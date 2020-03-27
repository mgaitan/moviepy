from moviepy.decorators import apply_to_mask


@apply_to_mask
def even_size(clip):
    """ 
    Crops the clip to make dimensions even.
    """
    w, h = clip.size
    w_even = w % 2 == 0
    h_even = h % 2 == 0
    if w_even and h_even:
        return clip

    def fl_image(a):
        if not w_even and not h_even:
            return a[:-1, :-1, :]
        elif w_even:
            return a[:, :-1, :]
        else:
            return a[:-1, :, :]

    return clip.fl_image(fl_image)
