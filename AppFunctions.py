

class AppFunctions:

    @staticmethod
    def generate_value_options():
        value_options = []
        for i in range(100, 1600, 100):
            value_options.append(i)
        return value_options

    @staticmethod
    def generate_estimation_options():
        estimation_options = []
        i = 0.5
        while i < 40.1:
            estimation_options.append(i)
            i += 0.5
        return estimation_options