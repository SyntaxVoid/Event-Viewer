from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg


class CustomToolbar(NavigationToolbar2TkAgg):
    # Creates a custom toolbar that only uses the buttons we want. Ideally,
    # this removes the forward, backward, and configure subplots button.
    toolitems = [t for t in NavigationToolbar2TkAgg.toolitems] #3if \
        #t[0] in ("Home", "Pan", "Zoom", "Save")]