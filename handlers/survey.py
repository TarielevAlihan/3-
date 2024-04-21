from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router()


# FSM - Finite State Machine - конечный автомат
class BookSurvey(StatesGroup):
    name = State()
    age = State()
    revew = State()
    data1 = State()
    question = State()
    question1= State()
    question2= State()
    end = State()



@survey_router.callback_query(F.data == "survey")
async def start_survey(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookSurvey.name)
    await cb.message.answer("Как вас зовут?")


@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer(f"Ваш номер телефона {message.text}?")

@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    await state.update_data(age=int(age))
    await state.set_state(BookSurvey.data1)
    await message.answer("Укажите ваш пол?")


@survey_router.message(BookSurvey.data1)
async def process_gender(message: types.Message, state: FSMContext):
    data1 = message.text
    if not data1.isdigit():
        await message.answer("пожалуста введите дату")
        return
    await state.update_data(data1=int(data1))
    await state.set_state(BookSurvey.revew)
    await message.answer("Дата вашего посещения нашего заведения")


@survey_router.message(BookSurvey.revew)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(revew=message.text)
    await state.set_state(BookSurvey.question)
    await message.answer("Как оцениваете качество еды")


@survey_router.message(BookSurvey.question)
async def process_questions(message: types.Message, state: FSMContext):
    await state.update_data(question=message.text)
    await state.set_state(BookSurvey.question1)
    await message.answer('Как оцениваете чистоту заведения')


@survey_router.message(BookSurvey.question1)
async def process_question(message: types.Message, state:FSMContext):
    await state.update_data(question1=message.text)
    await state.set_state(BookSurvey.question2)
    await message.answer('Дополнительные комментарии')


@survey_router.message(BookSurvey.question2)
async def process_question(message: types.Message, state:FSMContext):
    await state.update_data(question2=message.text)
    await state.set_state(BookSurvey.end)
    await message.answer('Спасибо за пройденый опрос')


@survey_router.message(BookSurvey.end)
async def process_end(message: types.Message, state : FSMContext):
    await state.update_data(end=message.text)
    await state.clear(BookSurvey.end)
