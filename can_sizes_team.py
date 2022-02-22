import math

radius = [6.83, 7.78, 8.73,	10.32, 10.79, 13.02	,5.40, 6.83, 15.72,	6.83, 7.62,	8.10]
heights = []
name = []




def main():
    # Your program must compute the volume of all 12 can sizes.
   
    
    volume = compute_volume()
    surface_area = compute_surface_area()
    storage_efficiency = compute_storage_efficiency()



    print(f"The volume for picnic 1 is: {one_picnic:.2f}")


def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    # volume = π radius2 height

    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius (radius + height)

    return surface_area

def compute_surface_efficiency(volume, surface_area)

    storage_efficiency = volume / surface_area

    return storage_efficiency

# surface_area = 2π radius (radius + height)
main()