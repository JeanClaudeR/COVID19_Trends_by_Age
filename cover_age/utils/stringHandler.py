"""
stringHandler: Wrangling strings data
=============================================

.. moduleauthor:: Jean-Claude RAZAFINDRAKOTO <jc.razafindrakoto@gmail.com>

"""

def delete_spaces(s):
    """Deletes all the spaces of a string

    Parameters:
    -----------
    s : str

    Returns
    -----------
        The corresponding string
    """
    s = ''.join(i for i in s if i != ' ')

    return s

if __name__== '__main__':
    assert delete_spaces("I love banana") == "Ilove banana", "failing, should get Ilovebanana"