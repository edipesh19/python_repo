#-------------------------------------------------------------------------------
# Name:        Data Type
# Purpose: Python has five standard datatypes
#           1. Number [int, long, float, complex]
#           2. String, 3. List, 4. Tuple, 5. Dictionary
#
# Author:     Dipesh Kumar Dutta
#
# Created:     11/05/2014
# Copyright:   (c) Dipesh 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
#1. Number type object creation. It is immutable
    var1 = 1;
    var2 = 10;

    # Deleting the number object
    del var1, var2

#2. String variable
    str1 = "Hello World!"
    print str1              # Hello World!
    print str1[0]           # H
    print str1[2:5]         # llo
    print str1[2:]          # llo World!
    print str1 * 2          # Hello World!Hello World!
    print str1 + "Python"   # Hello World!python

#3. List Variable
    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, 'john']

    print list              # Prints complete list
    print list[0]           # Prints first element of the list
    print list[1:3]         # Prints elements starting from 2nd till 3rd
    print list[2:]          # Prints elements starting from 3rd element
    print tinylist * 2      # Prints list two times
    print list + tinylist   # Prints concatenated lists

#4. Tuples. Same as list diff is enclosed with (). and is read only
    tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
    tinytuple = (123, 'john')

    print tuple             # Prints complete list
    print tuple[0]          # Prints first element of the list
    print tuple[1:3]        # Prints elements starting from 2nd till 3rd
    print tuple[2:]         # Prints elements starting from 3rd element
    print tinytuple * 2     # Prints list two times
    print tuple + tinytuple # Prints concatenated lists

    tuple[2] = 1000     # Invalid syntax with tuple because tuple is read only
    list[2] = 1000      # Valid syntax with list

#5. Dictionary: Python's dictionaries are kind of hash table type.
# A dictionary key can be almost any Python type, but are usually numbers or
# string. Values, on the other hand, can be any arbitrary Python object.
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"

    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

    print dict['one']       # Prints value for 'one' key
    print dict[2]           # Prints value for 2 key
    print tinydict          # Prints complete dictionary
    print tinydict.keys()   # Prints all the keys
    print tinydict.values() # Prints all the values


if __name__ == '__main__':
    main()
