#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx ", str[i]);
	}
	printf("\n");
}
