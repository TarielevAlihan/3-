from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from cofig import database

survey_router = Router()


# FSM - Finite State Machine - конечный автомат
class BookSurvey(StatesGroup):
    name = State()
    number_phone = State()
    revew = State()
    visit_data = State()
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
    await state.set_state(BookSurvey.number_phone)
    await message.answer(f"Ваш номер телефона {message.text}?")

@survey_router.message(BookSurvey.number_phone)
async def process_age(message: types.Message, state: FSMContext):
    number_phone = message.text
    if not number_phone.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    await state.update_data(age=int(number_phone))
    await state.set_state(BookSurvey.visit_data)
    await message.answer("Дата вашего посещения нашего заведения")


@survey_router.message(BookSurvey.visit_data)
async def process_gender(message: types.Message, state: FSMContext):
    visdata = message.text
    if not visdata.isdigit():
        await message.answer("пожалуста введите дату")
        return
    await state.update_data(data1=int(visdata))
    await state.set_state(BookSurvey.revew)
    await message.answer("Укажите ваш пол")


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
    await message.answer("Спасибо за пройденный опрос!")

@survey_router.message(BookSurvey.end)
async def process_end(message: types.Message, state : FSMContext):
    await state.update_data(end=message.text)
    data = await state.get_data()
    await database.execute(
        "INSERT INTO survey (name, age, data1, revew, question, question1, question2) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
        data["name"], data["age"], data["data1"], data["revew"], data["question"], data["question1"], data["question2"])
    )
    await message.answer("Спасибо за пройденный опрос!")
    await state.clear(BookSurvey.end)
