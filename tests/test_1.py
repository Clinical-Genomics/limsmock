from genologics.lims import Lims
from genologics.entities import Process, Sample

def test_A(server_test1):
    lims = Lims("http://127.0.0.1:8000", 'dummy', 'dummy')
    s = Sample(lims, id = 'ACC2351A1')
    assert s.udf['customer'] == 'cust002'

def test_B(server_test1):
    lims = Lims("http://127.0.0.1:8000", 'dummy', 'dummy')
    p = Process(lims, id = '24-168017')
    assert p.id == '24-168017'
    assert p.udf.items() == [('Instrument Used', 'Cava')]


    
