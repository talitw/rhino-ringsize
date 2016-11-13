from Rhino.DocObjects import *
from Rhino.Input import *
from Rhino.Commands import *
from Rhino.Geometry import *

import scriptcontext
import System.Guid
#this line with the name of the command:
__commandname__ = "RingSize"
def RunCommand( is_interactive ):
  rc, ringSize = RhinoGet.GetNumber("Ring size (US)?", False, 9)
  if rc <> Result.Success:
    return rc

  center = Point3d(0, 0, 0)
  radius = (11.63 + 0.8128 * ringSize) * 0.5
  c = Circle(center, radius)
  if scriptcontext.doc.Objects.AddCircle(c)!=System.Guid.Empty:
    scriptcontext.doc.Views.Redraw()
    return Result.Success
  return Result.Failure
