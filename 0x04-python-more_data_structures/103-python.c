#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - gives data of the PyBytesObject
 *
 * @obj: the PyObject
 */

void print_python_bytes(PyObject *obj)
{
	Py_ssize_t size = 0, i = 0;
	char *data = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(obj, &data, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", data);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (i < size + 1 && i < 10)
		{
			printf(" %02hhx", data[i]);
			i++;
		}
		printf("\n");
	}
}

/**
 * print_python_list - gives data of the PyListObject
 *
 * @obj: the PyObject
 */

void print_python_list(PyObject *obj)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	if (PyList_CheckExact(obj))
	{
		size = PyList_Size(obj);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)obj)->allocated);

		while (i < size)
		{
			item = PyList_GET_ITEM(obj, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			i++;
		}
	}
}
