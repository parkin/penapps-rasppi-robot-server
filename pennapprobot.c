/*  Example of wrapping cos function from math.h with the Python-C-API. */
#include <Python.h>
#include <stdio.h>

/*  wrapped cosine function */
static PyObject* turn_left(PyObject* self, PyObject* args)
{
	printf("turning left\n");
	return Py_BuildValue("d", 0);
}

/*  define functions in module */
static PyMethodDef methods[] =
{
	{"turn_left", turn_left, METH_VARARGS, "turn left"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef pennapprobotmodule = {
	PyModuleDef_HEAD_INIT,
	"pennapprobot",   /* name of module */
	NULL, /* module documentation, may be NULL */
	-1,       /* size of per-interpreter state of the module,
				                 or -1 if the module keeps state in global variables. */
	methods
};

/* module initialization */
PyMODINIT_FUNC

PyInit_pennapprobot(void)
{
	PyObject *m;

	m = PyModule_Create(&pennapprobotmodule);
	if (m == NULL)
		return NULL;
	return m;
}
