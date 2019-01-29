//
int $toggled_color
if($toggled_color == 0)
{
    displayRGBColor "background" 1. 1. 1.
    $toggled_color = 1
}
else
{
    displayRGBColor "background" 0.688 0.688 0.688
    $toggled_color = 0
}
//
