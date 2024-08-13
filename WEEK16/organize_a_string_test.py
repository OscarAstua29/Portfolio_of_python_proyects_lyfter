from organize_a_string_week06 import organize_string
def test_organize_string ():
        string =  'CASA-AUTO-DEDO-BEBE'
        result = organize_string(string)
        assert result == 'AUTO-BEBE-CASA-DEDO'