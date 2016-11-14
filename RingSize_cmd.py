import rhinoscriptsyntax as rs

__commandname__ = "RingSize"
def RunCommand( is_interactive ):
  ringSize = rs.GetReal("Ring size", 8.5, 0, 16)
  center = rs.GetPoint("Location")

  plane = rs.MovePlane(rs.ViewCPlane(), center)
  radius = (11.63 + 0.8128 * ringSize) * 0.5
  objId = rs.AddCircle(plane, radius)
  rs.SelectObject(objId)
