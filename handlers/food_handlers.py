from dataclasses import dataclass


@dataclass
class Food:

    # attributes
    _name: str = None
    _calories: float = None
    _fat: float = None
    _carbs: float = None
    _sugar: float = None
    _protein: float = None
    _tags: set[str] = None
    _serving_grams: float = None
    _serving_amount: float = None
    _serving_unit: str = None
    _servings_yield: float = None
    _ingredients: list = None
    _instructions: list = None
    _time_to_make: float = None
    _acquisition: set[str] = None
    _region: str = None


    # calories methods
    @property
    def calories(self):
        return self._calories


    @calories.setter
    def calories(self, new_calories):
        if new_calories > 0:
            self._calories = new_calories
        else:
            print("Please enter valid calories.")


    @calories.deleter
    def calories(self):
        del self._calories


    # fat methods
    @property
    def fat(self):
        return self._fat


    @fat.setter
    def fat(self, new_fat):
        if new_fat > 0:
            self._fat = new_fat
        else:
            print("Please enter valid fat.")


    @fat.deleter
    def fat(self):
        del self._fat


    # carbs methods
    @property
    def carbs(self):
        return self._carbs


    @carbs.setter
    def carbs(self, new_carbs):
        if new_carbs > 0:
            self._carbs = new_carbs
        else:
            print("Please enter valid carbs.")


    @carbs.deleter
    def carbs(self):
        del self._carbs


    # sugar methods
    @property
    def sugar(self):
        return self._sugar


    @sugar.setter
    def sugar(self, new_sugar):
        if new_sugar > 0:
            self._sugar = new_sugar
        else:
            print("Please enter valid sugar.")


    @sugar.deleter
    def sugar(self):
        del self._sugar


    # protein methods
    @property
    def protein(self):
        return self._protein


    @protein.setter
    def protein(self, new_protein):
        if new_protein > 0:
            self._protein = new_protein
        else:
            print("Please enter valid protein.")


    @protein.deleter
    def protein(self):
        del self._protein


    # serving grams methods
    @property
    def serving_grams(self):
        return self._serving_grams


    @serving_grams.setter
    def serving_grams(self, new_serving_grams):
        if new_serving_grams > 0:
            self._serving_grams = new_serving_grams
        else:
            print("Please enter valid serving_grams.")


    @serving_grams.deleter
    def serving_grams(self):
        del self._serving_grams
