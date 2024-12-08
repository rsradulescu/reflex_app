import reflex as rx
from . import routes

class NavState(rx.State):
    def to_home(selft):
        return rx.redirect(routes.HOME_ROUTE)
    def to_category(self):
        return rx.redirect(routes.CATEGORY_ROUTE)
    def to_element(self):
        return rx.redirect(routes.ELEMENT_ROUTE)
    def to_calendar(self):
        return rx.redirect(routes.CALENDAR_ROUTE)
    def to_notification(self):
        return rx.redirect(routes.NOTIFICATION_ROUTE)
    