from project import shelf, genre, len_arg
import pytest

def main():
    test_len_arg()
    test_genre()
    test_shelf()



def test_len_arg():
    with pytest.raises(SystemExit):
        len_arg()
    

def test_genre():
    assert genre("love") == "fiction"
    assert genre("method") == "science"
    assert genre("thinking") == "philosophy"
    assert genre("ontology") == "philosophy"
    assert genre("romance") == "fiction"



def test_shelf():
    assert shelf(111) == "2.shelf"





if __name__ == "__main__":
    main()