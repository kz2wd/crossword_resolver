# VERY IMPORTANT X => UP / DOWN  and Y => LEFT / RIGHT
# X + 1 => DOWN
# Y + 1 => RIGHT


class CrosswordResolver:
    def __init__(self, grid, words):
        self.grid = grid
        self.raw_size = len(self.grid[0])
        self.column_size = len(self.grid)
        self.words = words
        self.used_letters_grid = [[0 for j in range(self.raw_size)] for i in range(self.column_size)]

    def resolve(self):
        for word in self.words:
            word_letters = list(word)
            word_len = len(word)
            if word_len > 1:
                for x in range(self.column_size):
                    for y in range(self.raw_size):
                        if word_letters[0] == self.grid[x][y]:
                            directions = self.give_word_direction(x, y, word_letters[1])

                            if directions:
                                for direction in directions:
                                    word_is_found = True
                                    for i in range(word_len):
                                        letter_pos = (direction[0] * i, direction[1] * i)
                                        modified_x = x + letter_pos[0]
                                        modified_y = y + letter_pos[1]

                                        try:
                                            if word_letters[i] != self.grid[modified_x][modified_y]:
                                                word_is_found = False
                                        except IndexError:
                                            word_is_found = False

                                    if word_is_found:
                                        for i in range(word_len):
                                            letter_pos = (direction[0] * i, direction[1] * i)
                                            self.used_letters_grid[x + letter_pos[0]][y + letter_pos[1]] = 1

        end_letters = self.give_remaining_letters()
        print(" ".join(i for i in end_letters))

    def give_word_direction(self, x, y, next_letter):
        directions = []
        max_raw = self.raw_size - 1
        max_column = self.column_size - 1
        if x < max_raw:
            if self.grid[x + 1][y] == next_letter:
                directions.append((1, 0))  # down

            if y < max_column:
                if self.grid[x + 1][y + 1] == next_letter:
                    directions.append((1, 1))  # down right

        if x > 0:
            if self.grid[x - 1][y] == next_letter:
                directions.append((-1, 0))  # up

            if y < max_column:
                if self.grid[x - 1][y + 1] == next_letter:
                    directions.append((-1, 1))  # up right

        if y < max_column:
            if self.grid[x][y + 1] == next_letter:
                directions.append((0, 1))  # right

        if y > 0:
            if self.grid[x][y - 1] == next_letter:
                directions.append((0, -1))  # left
            if x < max_raw:
                if self.grid[x + 1][y - 1] == next_letter:
                    directions.append((1, -1))  # down left
            if x > 0:
                if self.grid[x - 1][y - 1] == next_letter:
                    directions.append((-1, -1))  # up left

        return directions

    def give_remaining_letters(self):
        letters_not_used = []

        for x in range(self.column_size):
            for y in range(self.raw_size):
                if self.used_letters_grid[x][y] == 0:
                    letters_not_used.append(self.grid[x][y])

        return letters_not_used


my_grid = ["P G D C D I A L H E A B L A",
           "M R N L R L T U I R K A Z A",
           "A A A I N E R H D P N A E I",
           "W I L A N R V N U D U T L O",
           "S N S H I T U A S N O P N S",
           "T H S C E T H L S R D A P R",
           "O J A E C C I G N S C E N T",
           "L N R E A D A A I L E I R Y",
           "E D G E E R D V O L A H F E",
           "O T S E R O F V E T C R U L",
           "T R E S E D N E N N H I L L",
           "R I V E R X P U E S N O W A",
           "M R O T S E O R T E E L S V",
           "C T R E E M T T F E E R E D"]

my_grid = [line.split(" ") for line in my_grid]

my_words = ["CAVE",
            "CREVASSE",
            "DESERT",
            "FOREST",
            "GRASSLAND",
            "HAIL",
            "HILL",
            "HURRICANE",
            "LAKE",
            "LANDSLIDE",
            "LIGHTNING",
            "MOUNTAIN",
            "PUPIL",
            "RAIN",
            "REEF",
            "RIVER",
            "SLEET",
            "SNOW",
            "STORM",
            "SWAMP",
            "THUNDER",
            "TORNADO",
            "TREE",
            "TRENCH",
            "TUNDRA",
            "VALLEY",
            "VOLCANO"]

CR = CrosswordResolver(my_grid, my_words)
CR.resolve()
