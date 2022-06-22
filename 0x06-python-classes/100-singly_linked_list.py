#!/usr/bin/python3
"""
Module import 100-singly_linked_list
Defines class node
Defines SinglyLinkedList class
"""


class Node:
    """Defines class node
    Args:
    data (int) : private instance
    next_node : private node or none
    Functions:
    __init__(self, data, next_node=None)
    data(self)
    data(self, value)
    next_node(self)
    next_node(self, value)
    """
    def __init__(self, data, next_node=None):
        """Initializes Node
        Attributes:
        data (int) : private instance
        next_node : private node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter
        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter
        Args:
        value: set data value
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter
        Return: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter
        Args:
        value: sets next_node if next_node or none
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines SinglyLinkedList class
    Args:
    head: private
    Functions:
    __init__(self)
    sorted_insert(self, value)
    """
    def __init__(self):
        """Initializes singlylinkedlist
        Attributes:
        head: private
        """
        self.__head = None

    def __str__(self):
        """SinglyLinkedList string representation."""
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """Insert new node into singly linked list.
        Args:
        value: data int for node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        temp = self.__head
        if new.data < temp.data:
            new.next_node = self.__head
            self.__head = new
            return
        while(temp.next_node is not None) and (new.data > temp.next_node.data):
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
        return
