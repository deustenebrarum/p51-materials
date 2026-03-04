// Как в математике f(x) = 2x, y = f(x)
function f(x) {
  return 2 * x;
}
const y = f(x);

// Код без функций

// получение данных пользователя
const data = JSON.parse(data);
const email = data["email"];
const password = data["password"];

// проверка правильности электронной почты
if (email.contains("@") && email.length > 5) {
  // подключение к базе данных
  const dbConnectionString = Environment.GetConnectionString();
  const db = DB.openConnection(dbConnectionString);

  // еще 3 строки для настройки подключения к базе данных

  // очистка вредного кода(SQL Injection) из данных пользователя
  const emailSanitized = DB.sanitize(email);
  const passwordSanitized = DB.sanitize(password);

  // запрос на создание пользователя в базе данных
  db.query(
    `INSERT INTO users(email, password) VALUES ` +
      `(${emailSanitized}), (${passwordSanitized})`,
  );

  // Подключение к почтовому серверу и отправка
  // сообщения о регистрации пользователю
  const smtp = smtp.Connect("DATA");
  // 5 строк настройки
  smtp.send(emailSanitized, "You have regitred");
}

// Код с функциями

const userData = getUserData(rawData);

if (isValidEmail(userData.email)) {
  const db = getDbConnection();

  const user = createUser(db, userData);

  notifyByEmail(user, "You have registered");
}

function age(yearOfBirth) {
  return new Date().getFullYear() - yearOfBirth;
}

const yearOfBirth = 2000;
const age = age(yearOfBirth);
