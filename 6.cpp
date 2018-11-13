/*
Challenge

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node. Implement
an XOR linked list; it has an add(element) which adds the element to the
end, and a get(index) which returns the node at index.
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.*/

//I'm using c++ here because python doesn't support pointer arithmetics
#include <string>
#include <iostream>
#include <stdexcept>
#include <assert.h>

struct Node
{
    std::string Value;
    intptr_t Both;
};

class XORList
{
    Node *_first = nullptr;
    Node *_last = nullptr;
    /*
	* Creates new node with no "next" value
	*/
    Node *NewNode(std::string value) const
    {
        auto node = new Node();
        node->Value = value;
        node->Both = reinterpret_cast<intptr_t>(_last) ^ 0;
        return node;
    }

  public:
    /*
	 * Returns value at index.
	 * 
	 * Complexity O(n)
	*/
    std::string Get(int index) const
    {
        //there are no elements in list.
        if (!_first)
            throw std::out_of_range("Index out of bounds.");
        //we are starting from first node
        auto current = reinterpret_cast<intptr_t>(_first),
             previous = 0,
             currentIndex = 0;
        do
        {
            //we found it
            if (currentIndex == index)
                return reinterpret_cast<Node *>(current)->Value;
            //move to next value
            auto tempCurrent = current;
            current = previous ^ reinterpret_cast<Node *>(current)->Both;
            previous = tempCurrent;

            currentIndex++;
        } while (current); //if current is 0 it means we traversed whole list

        throw std::out_of_range("Index out of bounds.");
    }
    /*
	 * Appends new value.
	 *
	 * Complexity O(1)
	 */
    void Insert(std::string value)
    {
        //create node
        auto node = NewNode(value);

        if (!_first) //if first node is null it means this is first value being inserted
            _first = node;
        else //otherwise if this isn't first value being inserted, we should update previously last nodes "Both" value with our new nodes memory location
            _last->Both = _last->Both ^ reinterpret_cast<intptr_t>(node);
        //sets our new node as last
        _last = node;
    }
};

int main(int argc, char const *argv[])
{
    XORList list;
    list.Insert("0");
    list.Insert("1");
    list.Insert("2");
    list.Insert("3");
    list.Insert("4");
    list.Insert("5");

    assert(list.Get(0) == "0");
    assert(list.Get(3) == "3");
    assert(list.Get(5) == "5");

    return 0;
}