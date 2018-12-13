#include "Python.h"

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_SIZE(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
