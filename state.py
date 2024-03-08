from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminStates(StatesGroup):
    add_book_state = State()