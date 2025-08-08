# https://github.com/scikit-mobility/scikit-mobility/issues/293
import pytest
from shapely.geometry import Polygon
try:
    from shapely.ops import cascaded_union  # Shapely < 2.0
except ImportError:
    from shapely.ops import unary_union as cascaded_union  # Shapely >= 2.0

def test_cascaded_union_basic():
    """Test cascaded_union with simple polygons"""
    poly1 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    poly2 = Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)])
    
    result = cascaded_union([poly1, poly2])
    assert result.is_valid
    assert result.area > poly1.area  # Union should be larger than individual polygons