# Lab2-FLCD
For my symbol table I had to implement 2 separate Hash Tables,one for identifiers and one for constants


1.getSize()-returns the size(int)
2.getItems()-returns the items(array)
3.hashCode(key)-returns the hash value(=position) of a specified element(=key),which will be computed as key % size
4.getValue(key)-returns the has value(=position) of a specified element(=key) if that one exists in the items list,None otherwise
5.addValue(key)-adds the element(=key) to the list.If the position is empty,it will just put the element.If the already exists,nothing happens.
                If the position is not empty,the element will be added at the end.
6.deleteValue(key)-if the element(=key) does not exist in the table,an error will occur,otherwise it will search through the elements of that position and it will delete the key

