function Car(model, maxFuelAmount, initialFuelAmount) {
  this.model = model;
  this.maxFuelAmount = maxFuelAmount;
  // TODO: default 0 instead of always 0
  if (initialFuelAmount != null) {
    this.currentFuelAmount = initialFuelAmount;
  } else {
    this.currentFuelAmount = 0;
  }
}

/**
 * @returns Amount of remained fuel after fueling
 **/
Car.prototype.tryAddFuel = function (amount) {
  if (amount < 0) {
    throw new Error("Amount of fuel can't be negative");
  }
  const remainTankSpace = this.maxFuelAmount - this.currentFuelAmount;
  if (amount <= remainTankSpace) {
    this.currentFuelAmount += amount;
    return 0;
  }
  this.currentFuelAmount = this.maxFuelAmount;
  return amount - remainTankSpace;
};

function GasStation(initialFuelAmount) {
  this.currentFuelAmount = initialFuelAmount;
}

/**
 * @argument car {Car}
 */
GasStation.prototype.fuelUp = function (car) {
  // Заправляем машину всем имеющимся топливом, получаем остаток
  const remainedFuel = car.tryAddFuel(this.currentFuelAmount);
  // Заменяем текущее количество топливо на оставшееся
  // после заправки
  this.currentFuelAmount = remainedFuel;
};

const car1 = new Car("Model1", 1000);
console.log(car1.tryAddFuel(900) === 0);
console.log(car1.tryAddFuel(50) === 0);
console.log(car1.currentFuelAmount === 950);

const car2 = new Car("Model1", 1000);
console.log(car2.tryAddFuel(1100) === 100);
console.log(car2.currentFuelAmount === 1000);

const gasStation = new GasStation(30);
gasStation.fuelUp(car1);
console.log(car1.currentFuelAmount === 980);
console.log(gasStation.currentFuelAmount === 0);

const gasStation1 = new GasStation(3000);
gasStation1.fuelUp(car1);
console.log(car1.currentFuelAmount === 1000);
console.log(gasStation1.currentFuelAmount === 2980);
