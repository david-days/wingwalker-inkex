#!/usr/bin/env python3

from typing import List
import inkex
import wingwalker as ww


X, Y = range(2)
airfoil_desig = "airfoil"


def drawAirfoil(xs, ys, offset, width,  parent):
    style = {"stroke": "#000000", "stroke-width": str(width), "fill": "none" }
    elem = parent.add(inkex.PathElement())
    # generate path definition
    fpath = "M " + str(xs[0] + offset[X]) + "," + str(ys[0] + offset[Y])
    for i in range(1,len(xs)):
            fpath += " L " + str(xs[i] + offset[X]) + "," + str(ys[i] + offset[Y])
    # close the loop
    fpath += " L " + str(xs[0] + offset[X]) + "," + str(ys[0]+offset[Y]) + " z"

    elem.update(
        **{
            "style": style,
            "inkscape:label": airfoil_desig,
            "d": fpath,
        }
    )
    return elem

    
class AirfoilExtension(inkex.InputExtension):

    input_ext = 'dat'
    output_ext = 'svg'

    xs,ys = [],[]
    c_len = 240.0
    dat_format = "selig"
    units = "mm"  
    
    def add_arguments(self, pars):
        pars.add_argument("--dat_format", type=str, default="selig")
        pars.add_argument("--c_len", type=float, default=240.0)
        pars.add_argument("--units", type=str, default="mm")


    def parse_arguments(self, args: List[str]) -> None:
        self.options = self.arg_parser.parse_args(args)
        self.dat_format = self.options.dat_format
        self.c_len = self.options.c_len
        self.units = self.options.units

    
    def load(self, stream):
        spec_name = ww.utils.parse_specs(stream, self.xs, self.ys, self.c_len, self.dat_format)
        print('Airfoil:  %s' % spec_name)
        print('Format:  %s' % self.dat_format)
        print('\tChord length:  %f %s' % (self.c_len, self.units))
        print('\tTotal X Coordinates:  %i' % len(self.xs))
        print('\tTotal Y Coordinates: %s' % (self.ys))


    def effect(self):
        self.document = self.get_template(width=self.c_len, height=self.c_len, unit=self.units)
        self.svg = self.document.getroot()

        p_layer = self.svg.get_current_layer()
        offset = self.svg.namedview.center
        stroke_width = self.svg.unittouu("2px")
        return drawAirfoil(self.xs, self.ys, offset, stroke_width, p_layer)
    

if __name__ == '__main__':
    AirfoilExtension().run()
