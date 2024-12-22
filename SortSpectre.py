# Author: Saqib Ashraf
# Date: 07/06/2023
# Purpose: a visualizer for various sorting algorithms

# These are all the imports that are being used for this program
import pygame #what will be used for the visualization
import random #random will be used for the bars that we are going to use to generate randomly to be sorted using various sorting algorithms
pygame.init() #used to initialize the pygame

#this is the holder class that is used for all the base measurements ( bar height, width, etc)

class Measurements:

    #these are just the global variables that are used for all the visualizations
    #______________________________________________________________________________________________________________________
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    RED_BLOOD = 136,8,8
    RED_BRIGHT = 238, 75, 43
    CHERRY = 210, 4, 45
    YELLOW = 255,255,0
    ROYAL_BLUE = 65,105,225
    BACKGROUND_COLOUR = BLACK
    SIDE_PADDING = 100  #this is the padding from the left and the right of the screen
    TOP_PADDING = 150
    FONT = pygame.font.SysFont('DroidSans', 30)
    SMALL_FONT = pygame.font.SysFont('DroidSans', 25)
    LARGE_FONT = pygame.font.SysFont('comic sans', 40)
    Gradients = [
        RED_BLOOD,
        RED_BRIGHT,
        CHERRY
    ]
    #________________________________________________________________________________________________________________________________

    def __init__(self, width, height, list):  #this is a the constructor for the class that auto generates the measurements
        self.width = width
        self.height = height
        self.set_list(list)  #this creates an instance of the list, where the list is being passed through the function "set_list"

        self.window = pygame.display.set_mode((width, height))  #this is the window that will be used for the visualization
        pygame.display.set_caption("Sorting Algorithms Visualizer - By: Saqib Ashraf")  #this is the title of the page, with the name

    def set_list(self, list):  #this is the method that sets the boundaries of the list, and allows it to stay in the bounds of the screen
        self.list = list
        self.min_val = min(list)
        self.max_val = max(list)
        #the following operation allows the code to draw whilst leaving the white spots on the side, dividing by the # of blocks (length of list)
        self.block_width = round((self.width - self.SIDE_PADDING) / len(list))
        #the following operation allows us to find the total drawable area, dividing by the range of values that we have, allowing us to not go over the screen
        self.block_height = int((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PADDING // 2
        # This stuff, do not touch it cuz there is no point of doing it twice


#this function is used to generate the list, using the random generator, this is the list that is being sorted
def generate_starting_list(n, min_val, max_val):

    list = []
    for _ in range(n):  #runs the loop for the amount of elements in the list
        val = random.randint(min_val, max_val)  #creates a random value
        list.append(val)  #this just adds the value to the end of the list
    return list


#this is the drawing function that is used to draw the nice visual components of the page
def Draw(draw_info, sorting_algorithm_name, acending):
    #this is the fill for the window, and allows for the window to be the background color that is set
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)

    #this is for the title of the page, with the name of the algorithm
    title = draw_info.FONT.render(f"{sorting_algorithm_name} - {'Acending' if acending else 'Decending'} - {TimeComplexity(sorting_algorithm_name, acending)}", 1, draw_info.WHITE)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    #this is for the user to know what the controls are for the game
    controls = draw_info.FONT.render(" R  - RESET | SPACE - START SORTING! | A - ACENDING | D - DECENDING", 1, draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 35))

    #these buttons actually initiate the sorting algorithm
    sorting = draw_info.SMALL_FONT.render("CHOOSE TYPE OF SORT:  I - INSERTION | B - BUBBLE  | G - COUNTING | S - SELECTION  | C - SHELL | M - MERGE", 1, draw_info.WHITE)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 65))

    #this function draws the list
    Draw_List(draw_info)

    #this constantly updates the window
    pygame.display.update()


#this function is used to display the time complexity of the sorting algorithm that is being used.
def TimeComplexity(sorting_algorithm_name, acending):
    if sorting_algorithm_name == "BUBBLE SORT":
        return "O(n^2)"
    elif sorting_algorithm_name == "INSERTION SORT":
        return "O(n^2)"
    elif sorting_algorithm_name == "MERGE SORT":
        return "O(nlogn)"
    elif sorting_algorithm_name == "QUICK SORT":
        return "O(nlogn)"
    elif sorting_algorithm_name == "HEAP SORT":
        return "O(nlogn)"
    elif sorting_algorithm_name == "SELECTION SORT":
        return "O(n^2)"
    elif sorting_algorithm_name == "SHELL SORT":
        return "O(n logn)"
    elif sorting_algorithm_name == "COUNTING SORT":
        return "O(n + k)"
    elif sorting_algorithm_name == "MERGE SORT":
        return "O(n logn)"


#this is used to draw the list, for the person to actually visualize.
def Draw_List(draw_info, colour_positions={}, clear_background=False):
    list = draw_info.list  #for better code readability

    if clear_background:
        clear_rectangle = (draw_info.SIDE_PADDING // 2, draw_info.TOP_PADDING, draw_info.width - draw_info.SIDE_PADDING, draw_info.height - draw_info.TOP_PADDING)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOUR, clear_rectangle)
        #this is to clear the background, without clearing everything, it is used to clear only a little bit of the background, without clearing all the lists

    for i, val in enumerate(list):  #enumerate gets the value and index
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        colour = draw_info.Gradients[i % 3]

        if i in colour_positions:
            colour = colour_positions[i]

        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.block_width, draw_info.height))

    if clear_background:
        pygame.display.update()


#this is just a regular bubble sort function
def Bubble_Sort(draw_info, acending=True):
    lst = draw_info.list

    for i in range(0, len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and acending) or (num1 < num2 and not acending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                Draw_List(draw_info, {j: draw_info.GREEN, j + 1: draw_info.YELLOW}, True)
                yield True
    return lst


#regular insertion sort
def Insertion_Sort(draw_info, acending=True):
    lst = draw_info.list
    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            acending_sort = i > 0 and lst[i - 1] > current and acending
            descending_sort = i > 0 and lst[i - 1] < current and not acending
            if not acending_sort and not descending_sort:
                break
            lst[i] = lst[i - 1]
            i -= 1
            lst[i] = current
            Draw_List(draw_info, {i - 1: draw_info.GREEN, i: draw_info.YELLOW}, True)
            yield True
    return lst


#regular selection sort
def Selection_Sort(draw_info, ascending=True):
    lst = draw_info.list
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if ascending:
                if lst[j] < lst[min_index]:
                    min_index = j
            else:
                if lst[j] > lst[min_index]:
                    min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

        if ascending:
            colors = {i: draw_info.GREEN, min_index: draw_info.YELLOW}
        else:
            colors = {i: draw_info.YELLOW, min_index: draw_info.GREEN}

        Draw_List(draw_info, colors, True)
        yield True

    return lst


#regular shell sort
def Shell_Sort(draw_info, ascending=True):
    lst = draw_info.list

    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i - gap
            while j >= 0 and (lst[j] > temp if ascending else lst[j] < temp):
                lst[j + gap] = lst[j]
                j -= gap
            lst[j + gap] = temp
        gap = gap // 2
        colors = {i: draw_info.GREEN for i in range(gap, n)} if ascending else {i: draw_info.GREEN for i in range(n - gap)}
        Draw_List(draw_info, colors, True)
        yield True
    return lst


#regular counting sort
def Counting_Sort(draw_info, ascending=True):
    lst = draw_info.list
    max_val = max(lst)

    count = [0] * (max_val + 1)
    output = [0] * len(lst)

    for x in lst:
        count[x] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    for x in lst:
        output[count[x] - 1] = x
        count[x] -= 1
        colors = {x: draw_info.GREEN, count[x]: draw_info.YELLOW} if ascending else {x: draw_info.YELLOW, count[x]: draw_info.GREEN}
        Draw_List(draw_info, colors, clear_background=True)
        yield True

    if not ascending:
        output.reverse()

    draw_info.list = output

    return output

#regular merge sort
def Merge_Sort(draw_info, acsending=True):
    lst = draw_info.list
    
    def merge_sort_recursion(ls, start, end):
        if start < end:
            mid = (start + end)//2
            yield from merge_sort_recursion(ls, start, mid)
            yield from merge_sort_recursion(ls, mid+1, end)
            yield from merge(ls, start, mid, end)
            
    def merge(ls, start, mid, end):
        n1 = mid - start + 1
        n2 = end - mid

        l = [ls[start + i] for i in range(n1)]
        r = [ls[mid + 1 + j] for j in range(n2)]

        i = j = 0
        k = start

        while i < n1 and j < n2:
            if l[i] <= r[j]:
                ls[k] = l[i]
                i += 1
            else:
                ls[k] = r[j]
                j += 1
            Draw_List(draw_info, {k: draw_info.GREEN}, clear_background=True)
            yield True
            k += 1

        while i < n1:
            ls[k] = l[i]
            i += 1
            k += 1
            Draw_List(draw_info, {k - 1: draw_info.GREEN}, clear_background=True)
            yield True

        while j < n2:
            ls[k] = r[j]
            j += 1
            k += 1
            Draw_List(draw_info, {k - 1: draw_info.YELLOW}, clear_background=True)
            yield True
    yield from merge_sort_recursion(lst, 0, len(lst) - 1)
        
#main that runs all the functions
def main():
    run = True
    clock = pygame.time.Clock()
    n = 35
    min_val = 0
    max_val = 100

    list = generate_starting_list(n, min_val, max_val)

    draw_info = Measurements(1000, 800, list)  #stores the whole class and allows it to be called everywhere that it is needed
    acending = True
    sorting = False

    sorting_algorithm = Bubble_Sort
    sorting_algorithm_name = "BUBBLE SORT"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False

        else:
            Draw(draw_info, sorting_algorithm_name, acending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                list = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(list)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, acending)
            elif event.key == pygame.K_a and not sorting:
                acending = True
            elif event.key == pygame.K_d and not sorting:
                acending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = Insertion_Sort
                sorting_algorithm_name = "INSERTION SORT"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = Bubble_Sort
                sorting_algorithm_name = "BUBBLE SORT"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = Selection_Sort
                sorting_algorithm_name = "SELECTION SORT"
            elif event.key == pygame.K_c and not sorting:
                sorting_algorithm = Shell_Sort
                sorting_algorithm_name = "SHELL SORT"
            elif event.key == pygame.K_g and not sorting:
                sorting_algorithm = Counting_Sort
                sorting_algorithm_name = "COUNTING SORT"
            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = Merge_Sort
                sorting_algorithm_name = "MERGE SORT"

    pygame.quit()


if __name__ == "__main__":
    main()
