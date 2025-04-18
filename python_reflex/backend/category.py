import reflex as rx
from typing import List, Optional
from sqlmodel import select, asc, desc, or_, func, Relationship, Field
from datetime import datetime, timedelta


class Subcategory(rx.Model, table=True):
    """The subcategory model."""
    name: str
    description: str
    date_added: str
    category_id: int = Field(foreign_key="category.id")
    category: Optional["Category"] = Relationship(
        back_populates="subcategories"
    )


class Category(rx.Model, table=True):
    """The category model."""
    name: str
    description: str
    date: str
    subcategories: List[Subcategory] = Relationship(
        back_populates="category"
    )


class State(rx.State):
    """The app state."""

    categories: list[Category] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_category: Category = Category()


    def load_entries(self) -> list[Category]:
        """Get all categories from the database."""
        with rx.session() as session:
            query = select(Category)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Category, field).ilike(search_value)
                            for field in Category.get_fields()
                            if field not in ["id"]
                        ],
                        # ensures that int/float values is cast to a string before applying the ilike operator
                        #cast(Category.payments, String).ilike(search_value),
                    )
                )

            if self.sort_value:
                sort_column = getattr(Category, self.sort_value)
                order = (
                    desc(func.lower(sort_column))
                    if self.sort_reverse
                    else asc(func.lower(sort_column))
                )
                query = query.order_by(order)

            self.categories = session.exec(query).all()

    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def get_category(self, category: Category):
        self.current_category = category

    def add_category_to_db(self, form_data: dict):
        self.current_category = form_data
        self.current_category["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with rx.session() as session:
            if session.exec(
                select(Category).where(Category.name == self.current_category["name"])
            ).first():
                return rx.window_alert("Category with this name already exists")
            session.add(Category(**self.current_category))
            session.commit()
        self.load_entries()
        return rx.toast.info(
            f"Category {self.current_category['name']} has been added.", position="bottom-right"
        )

    def update_category_to_db(self, form_data: dict):
        self.current_category.update(form_data)
        with rx.session() as session:
            category = session.exec(
                select(Category).where(Category.id == self.current_category["id"])
            ).first()
            for field in Category.get_fields():
                if field != "id":
                    setattr(category, field, self.current_category[field])
            session.add(category)
            session.commit()
        self.load_entries()
        return rx.toast.info(
            f"Category {self.current_category['name']} has been modified.",
            position="bottom-right",
        )

    def delete_category(self, id: int):
        """Delete a category from the database."""
        with rx.session() as session:
            category = session.exec(select(Category).where(Category.id == id)).first()
            session.delete(category)
            session.commit()
        self.load_entries()
        return rx.toast.info(
            f"Category {category.name} has been deleted.", position="bottom-right"
        )