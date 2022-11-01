#!/usr/bin/python3
""" Unit tests for AirBnB console """

import unittest
from unittest.mock import patch
import console
import pep8
import sys
from io import StringIO
import os
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Amenity(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(console.HBNBCommand.__doc__)

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("quit")
        value = fd.getvalue()
        self.assertEqual(value, "")

    def test_emptyline(self):
        """test for emptyline"""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("")
        value = fd.getvalue()
        self.assertEqual(value, "")

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("EOF")
        value = fd.getvalue()
        self.assertEqual(value, "")

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("create")
        value = fd.getvalue()
        self.assertEqual(value, "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("create Bsadkld")
        value = fd.getvalue()
        self.assertEqual(value, "** class doesn't exist **\n")

    def test_show(self):
        """Test show command."""
        n_bm = BaseModel()
        bmid = n_bm.id
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("show")
        value = fd.getvalue()
        self.assertEqual(value, "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("show Bsadkld")
        value = fd.getvalue()
        self.assertEqual(value, "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("show BaseModel")
        value = fd.getvalue()
        self.assertEqual(value, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("show BaseModel {}+1".format(bmid))
        value = fd.getvalue()
        self.assertEqual(value, "** no instance found **\n")

    def test_destroy(self):
        """Test destroy command."""
        n_bm = BaseModel()
        bmid = n_bm.id
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("destroy")
        value = fd.getvalue()
        self.assertEqual(value, "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("destroy Bsadkld")
        value = fd.getvalue()
        self.assertEqual(value, "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("destroy BaseModel")
        value = fd.getvalue()
        self.assertEqual(value, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("destroy BaseModel {}+1".format(bmid))
        value = fd.getvalue()
        self.assertEqual(value, "** no instance found **\n")

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("all Bsadkld")
        value = fd.getvalue()
        self.assertEqual(value, "** class doesn't exist **\n")

    def test_update(self):
        """Test update command."""
        n_bm = BaseModel()
        bmid = n_bm.id
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("update")
        value = fd.getvalue()
        self.assertEqual(value, "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("update Bsadkld")
        value = fd.getvalue()
        self.assertEqual(value, "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("update BaseModel")
        value = fd.getvalue()
        self.assertEqual(value, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("update BaseModel {}+1".format(bmid))
        value = fd.getvalue()
        self.assertEqual(value, "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("update BaseModel {}".format(bmid))
        value = fd.getvalue()
        self.assertEqual(value, "** attribute name missing **\n")

        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("update BaseModel {} sadsa ".format(bmid))
        value = fd.getvalue()
        self.assertEqual(value, "** value missing **\n")


if __name__ == "__main__":
    unittest.main()
