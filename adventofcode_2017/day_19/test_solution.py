import pytest

from .solution import solve

DATA_ABCDEF = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+   
                  
"""  # noqa
DATA_A = """
     |          
     |         
     A                  
"""  # noqa
DATA_AB = """
     |          
     |          
     A          
     |          
     |          
     +B           
"""  # noqa


@pytest.mark.parametrize(
    'data, seq, n',
    (
        (DATA_A, 'A', 3),
        (DATA_AB, 'AB', 7),
        (DATA_ABCDEF, 'ABCDEF', 38),
    )
)
def test_solve(data, seq, n):
    assert solve(data) == (seq, n)
