def max_water(height):
    """
    Finds the maximum water container area.
    Uses two-pointer optimization.
    """

    left = 0
    right = len(height) - 1

    max_area = 0


    while left < right:

        current_height = min(
            height[left],
            height[right]
        )

        width = right - left

        area = current_height * width


        max_area = max(
            max_area,
            area
        )


        # Move shorter line because it limits the area
        if height[left] < height[right]:

            left += 1

        else:

            right -= 1


    return max_area



# Testing

print(
    max_water(
        [1,8,6,2,5,4,8,3,7]
    )
)

print(
    max_water([1,1])
)