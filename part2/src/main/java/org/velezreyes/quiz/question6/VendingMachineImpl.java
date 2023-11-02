package org.velezreyes.quiz.question6;

import java.util.ArrayList;

//  Hacemos que implemente de la Interface Vending Machine
public class VendingMachineImpl implements VendingMachine {

  // generamos la variable de tipo VendingMachine para crear la instancia.
  private static VendingMachine machine;
  private static Integer money = 0;
  // Cramos tambien una vara
  private static ArrayList<Drink> drinks = new ArrayList<>();

  public static VendingMachine getInstance() {
    // Si ya existe una instancia, retornamos esta
    if (machine == null) {
      // Cuando creemo la instancia, le bebidas comienzan a estar dispoibles
      Drink ScottCola = new Drink() {
        @Override
        public String getName() {
          String name = "ScottCola";
          return name;
        }

        @Override
        public boolean isFizzy() {
          Boolean Fizzy = true;
          return Fizzy;
        }

        // public Integer getPrice() {
        // Integer price_drink = 75;
        // return price_drink;
        // }
      };

      Drink KarenTea = new Drink() {
        @Override
        public String getName() {
          String name = "KarenTea";
          return name;
        }

        @Override
        public boolean isFizzy() {
          Boolean Fizzy = false;
          return Fizzy;
        }

        // public Integer getPrice() {
        // Integer price_drink = 75;
        // return price_drink;
        // }
      };
      drinks.add(ScottCola);
      drinks.add(KarenTea);
      machine = new VendingMachineImpl();
    }
    return machine;
  }

  // Añadimos los metodos de la interface para usarlas
  @Override
  public void insertQuarter() {
    // Cada vez que se ingresa una moneda (una moneda de 25 centavos) aumenta el
    // contador de
    // dinero de la maquina.
    money += 25;
  }

  // nos traemos este tambien ademas de que tengamos en cuenta que puede arrojar
  // las excepciones
  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    for (Drink drink : drinks) {
      if (drink.getName().equals(name)) {
        Integer price;
        if (name.equals("ScottCola")) {
          price = 75;
        } else {
          price = 100;
        }
        if (money >= price) {
          money -= price;
          return drink;
        } else {
          throw new NotEnoughMoneyException();
        }
      }
    }
    throw new UnknownDrinkException();
  }
}
