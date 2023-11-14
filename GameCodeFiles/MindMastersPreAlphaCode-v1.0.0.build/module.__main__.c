/* Generated code for Python module '__main__'
 * created by Nuitka version 1.8.6
 *
 * This code is in part copyright 2023 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "nuitka/unfreezing.h"

#include "__helpers.h"

/* The "module___main__" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module___main__;
PyDictObject *moduledict___main__;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[53];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[53];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(PyThreadState *tstate) {
    if (constants_created == false) {
        loadConstantsBlob(tstate, &mod_consts[0], UNTRANSLATE("__main__"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 53; i++) {
            mod_consts_hash[i] = DEEP_HASH(tstate, mod_consts[i]);
        }
#endif
    }
}

// We want to be able to initialize the "__main__" constants in any case.
#if 1
void createMainModuleConstants(PyThreadState *tstate) {
    createModuleConstants(tstate);
}
#endif

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants___main__(PyThreadState *tstate) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 53; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(tstate, mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_e684cc165ccdfe28d115fd98d1c72d0a;
/* For use in "MainProgram.c". */
PyCodeObject *codeobj_main = NULL;

static void createModuleCodeObjects(void) {
    module_filename_obj = mod_consts[1]; CHECK_OBJECT(module_filename_obj);
    codeobj_e684cc165ccdfe28d115fd98d1c72d0a = MAKE_CODE_OBJECT(module_filename_obj, 1, 0, mod_consts[52], mod_consts[52], NULL, NULL, 0, 0, 0);
    codeobj_main = codeobj_e684cc165ccdfe28d115fd98d1c72d0a;
}

// The module function declarations.


// The module function definitions.


extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();

extern PyTypeObject Nuitka_Loader_Type;

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
// Provide a way to create find a function via its C code and create it back
// in another process, useful for multiprocessing extensions like dill
extern void registerDillPluginTables(PyThreadState *tstate, char const *module_name, PyMethodDef *reduce_compiled_function, PyMethodDef *create_compiled_function);

function_impl_code functable___main__[] = {

    NULL
};

static char const *_reduce_compiled_function_argnames[] = {
    "func",
    NULL
};

static PyObject *_reduce_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject *func;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:reduce_compiled_function", (char **)_reduce_compiled_function_argnames, &func, NULL)) {
        return NULL;
    }

    if (Nuitka_Function_Check(func) == false) {
        PyThreadState *tstate = PyThreadState_GET();

        SET_CURRENT_EXCEPTION_TYPE0_STR_STATE(tstate, PyExc_TypeError, "not a compiled function");
        return NULL;
    }

    struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)func;

    function_impl_code *current = functable___main__;
    int offset = 0;

    while (*current != NULL) {
        if (*current == function->m_c_code) {
            break;
        }

        current += 1;
        offset += 1;
    }

    if (*current == NULL) {
        PyThreadState *tstate = PyThreadState_GET();

        SET_CURRENT_EXCEPTION_TYPE0_STR(tstate, PyExc_TypeError, "Cannot find compiled function in module.");
        return NULL;
    }

    PyObject *code_object_desc = MAKE_TUPLE_EMPTY(6);
    PyTuple_SET_ITEM0(code_object_desc, 0, function->m_code_object->co_filename);
    PyTuple_SET_ITEM0(code_object_desc, 1, function->m_code_object->co_name);
    PyTuple_SET_ITEM(code_object_desc, 2, PyLong_FromLong(function->m_code_object->co_firstlineno));
    PyTuple_SET_ITEM0(code_object_desc, 3, function->m_code_object->co_varnames);
    PyTuple_SET_ITEM(code_object_desc, 4, PyLong_FromLong(function->m_code_object->co_argcount));
    PyTuple_SET_ITEM(code_object_desc, 5, PyLong_FromLong(function->m_code_object->co_flags));

    CHECK_OBJECT_DEEP(code_object_desc);

    PyObject *result = MAKE_TUPLE_EMPTY(4);
    PyTuple_SET_ITEM(result, 0, PyLong_FromLong(offset));
    PyTuple_SET_ITEM(result, 1, code_object_desc);
    PyTuple_SET_ITEM0(result, 2, function->m_defaults);
    PyTuple_SET_ITEM0(result, 3, function->m_doc != NULL ? function->m_doc : Py_None);

    CHECK_OBJECT_DEEP(result);

    return result;
}

static PyMethodDef _method_def_reduce_compiled_function = {"reduce_compiled_function", (PyCFunction)_reduce_compiled_function,
                                                           METH_VARARGS | METH_KEYWORDS, NULL};

static char const *_create_compiled_function_argnames[] = {
    "func",
    "code_object_desc",
    "defaults",
    "doc",
    NULL
};


static PyObject *_create_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    CHECK_OBJECT_DEEP(args);

    PyObject *func;
    PyObject *code_object_desc;
    PyObject *defaults;
    PyObject *doc;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO:create_compiled_function", (char **)_create_compiled_function_argnames, &func, &code_object_desc, &defaults, &doc, NULL)) {
        return NULL;
    }

    int offset = PyLong_AsLong(func);

    if (offset == -1 && HAS_ERROR_OCCURRED(tstate)) {
        return NULL;
    }

    if (offset > sizeof(functable___main__) || offset < 0) {
        SET_CURRENT_EXCEPTION_TYPE0_STR_STATE(tstate, PyExc_TypeError, "Wrong offset for compiled function.");
        return NULL;
    }

    PyObject *filename = PyTuple_GET_ITEM(code_object_desc, 0);
    PyObject *function_name = PyTuple_GET_ITEM(code_object_desc, 1);
    PyObject *line = PyTuple_GET_ITEM(code_object_desc, 2);
    int line_int = PyLong_AsLong(line);
    assert(!HAS_ERROR_OCCURRED(tstate));

    PyObject *argnames = PyTuple_GET_ITEM(code_object_desc, 3);
    PyObject *arg_count = PyTuple_GET_ITEM(code_object_desc, 4);
    int arg_count_int = PyLong_AsLong(arg_count);
    assert(!HAS_ERROR_OCCURRED(tstate));
    PyObject *flags = PyTuple_GET_ITEM(code_object_desc, 5);
    int flags_int = PyLong_AsLong(flags);
    assert(!HAS_ERROR_OCCURRED(tstate));

    PyCodeObject *code_object = MAKE_CODE_OBJECT(
        filename,
        line_int,
        flags_int,
        function_name,
        function_name, // TODO: function_qualname
        argnames,
        NULL, // freevars
        arg_count_int,
        0, // TODO: Missing kw_only_count
        0 // TODO: Missing pos_only_count
    );

    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        functable___main__[offset],
        code_object->co_name,
#if PYTHON_VERSION >= 0x300
        NULL, // TODO: Not transferring qualname yet
#endif
        code_object,
        defaults,
#if PYTHON_VERSION >= 0x300
        NULL, // kwdefaults are done on the outside currently
        NULL, // TODO: Not transferring annotations
#endif
        module___main__,
        doc,
        NULL,
        0
    );

    return (PyObject *)result;
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS | METH_KEYWORDS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode___main__(PyThreadState *tstate, PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("__main__");

    // Store the module for future use.
    module___main__ = module;

    // Modules can be loaded again in case of errors, avoid the init being done again.
    static bool init_done = false;

    if (init_done == false) {
#if defined(_NUITKA_MODULE) && 1
        // In case of an extension module loaded into a process, we need to call
        // initialization here because that's the first and potentially only time
        // we are going called.

        // Initialize the constant values used.
        _initBuiltinModule();
        createGlobalConstants(tstate);

        /* Initialize the compiled types of Nuitka. */
        _initCompiledCellType();
        _initCompiledGeneratorType();
        _initCompiledFunctionType();
        _initCompiledMethodType();
        _initCompiledFrameType();

        _initSlotCompare();
#if PYTHON_VERSION >= 0x270
        _initSlotIterNext();
#endif

        patchTypeComparison();

        // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
        PRINT_STRING("__main__: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader(tstate);

#if PYTHON_VERSION >= 0x300
        patchInspectModule(tstate);
#endif

#endif

        /* The constants only used by this module are created now. */
        NUITKA_PRINT_TRACE("__main__: Calling createModuleConstants().\n");
        createModuleConstants(tstate);

        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in init__main__\n");

    moduledict___main__ = MODULE_DICT(module___main__);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    registerDillPluginTables(tstate, loader_entry->name, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict___main__,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 1
        UPDATE_STRING_DICT0(
            moduledict___main__,
            (Nuitka_StringObject *)const_str_plain___package__,
            Py_None
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict___main__,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict___main__,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict___main__,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module___main__);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !1
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

    UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 1
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, _spec_from_module, module___main__);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(tstate, spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    PyObject *tmp_for_loop_1__for_iterator = NULL;
    PyObject *tmp_for_loop_1__iter_value = NULL;
    struct Nuitka_FrameObject *frame_e684cc165ccdfe28d115fd98d1c72d0a;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;
    bool tmp_result;
    PyObject *tmp_inplace_orig;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Module code.
    frame_e684cc165ccdfe28d115fd98d1c72d0a = MAKE_MODULE_FRAME(codeobj_e684cc165ccdfe28d115fd98d1c72d0a, module___main__);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_e684cc165ccdfe28d115fd98d1c72d0a);
    assert(Py_REFCNT(frame_e684cc165ccdfe28d115fd98d1c72d0a) == 2);

    // Framed code:
    {
        PyObject *tmp_imported_value_1;
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 1;
        tmp_imported_value_1 = IMPORT_HARD_SITE();
        if (tmp_imported_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = mod_consts[1];
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[2], tmp_assign_source_2);
    }
    {
        PyObject *tmp_assign_source_3;
        tmp_assign_source_3 = Py_None;
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[3], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        tmp_assign_source_4 = MAKE_DICT_EMPTY();
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[4], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[5];
        tmp_globals_arg_value_1 = (PyObject *)moduledict___main__;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = Py_None;
        tmp_level_value_1 = mod_consts[6];
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 1;
        tmp_assign_source_5 = IMPORT_MODULE5(tstate, tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_assign_source_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_name_value_2;
        PyObject *tmp_globals_arg_value_2;
        PyObject *tmp_locals_arg_value_2;
        PyObject *tmp_fromlist_value_2;
        PyObject *tmp_level_value_2;
        tmp_name_value_2 = mod_consts[7];
        tmp_globals_arg_value_2 = (PyObject *)moduledict___main__;
        tmp_locals_arg_value_2 = Py_None;
        tmp_fromlist_value_2 = Py_None;
        tmp_level_value_2 = mod_consts[6];
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 2;
        tmp_assign_source_6 = IMPORT_MODULE5(tstate, tmp_name_value_2, tmp_globals_arg_value_2, tmp_locals_arg_value_2, tmp_fromlist_value_2, tmp_level_value_2);
        assert(!(tmp_assign_source_6 == NULL));
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[7], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;
        tmp_assign_source_7 = Py_True;
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[8], tmp_assign_source_7);
    }
    {
        PyObject *tmp_assign_source_8;
        tmp_assign_source_8 = DEEP_COPY_LIST_GUIDED(tstate, mod_consts[9], "ddddddddddddddddddddddddddddddd");
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[10], tmp_assign_source_8);
    }
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[5]);
        }

        assert(!(tmp_expression_value_1 == NULL));
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_1, mod_consts[11]);
        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 132;

            goto frame_exception_exit_1;
        }
        tmp_args_element_value_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[10]);

        if (unlikely(tmp_args_element_value_1 == NULL)) {
            tmp_args_element_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[10]);
        }

        if (tmp_args_element_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_1);

            exception_lineno = 132;

            goto frame_exception_exit_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 132;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_called_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 132;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    loop_start_1:;
    {
        bool tmp_condition_result_1;
        PyObject *tmp_operand_value_1;
        tmp_operand_value_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_operand_value_1 == NULL)) {
            tmp_operand_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_operand_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto frame_exception_exit_1;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_1);
        if (tmp_res == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto frame_exception_exit_1;
        }
        tmp_condition_result_1 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_1 != false) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    goto loop_end_1;
    branch_no_1:;
    {
        PyObject *tmp_assign_source_9;
        tmp_assign_source_9 = mod_consts[12];
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[13], tmp_assign_source_9);
    }
    {
        PyObject *tmp_assign_source_10;
        tmp_assign_source_10 = mod_consts[6];
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[14], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;
        tmp_assign_source_11 = mod_consts[15];
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[16], tmp_assign_source_11);
    }
    {
        PyObject *tmp_called_value_2;
        PyObject *tmp_call_result_2;
        tmp_called_value_2 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_2 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 138;
        tmp_call_result_2 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_2);
        if (tmp_call_result_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 138;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_2);
    }
    {
        PyObject *tmp_assign_source_12;
        PyObject *tmp_input_arg_1;
        tmp_input_arg_1 = mod_consts[18];
        tmp_assign_source_12 = BUILTIN_INPUT(tstate, tmp_input_arg_1);
        if (tmp_assign_source_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 139;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[19], tmp_assign_source_12);
    }
    {
        PyObject *tmp_called_value_3;
        PyObject *tmp_call_result_3;
        tmp_called_value_3 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_3 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 140;
        tmp_call_result_3 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_3);
        if (tmp_call_result_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 140;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_3);
    }
    {
        PyObject *tmp_called_value_4;
        PyObject *tmp_call_result_4;
        tmp_called_value_4 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_4 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 141;
        tmp_call_result_4 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_4, mod_consts[20]);

        if (tmp_call_result_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 141;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_4);
    }
    {
        PyObject *tmp_called_value_5;
        PyObject *tmp_call_result_5;
        tmp_called_value_5 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_5 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 142;
        tmp_call_result_5 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_5, mod_consts[20]);

        if (tmp_call_result_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 142;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_5);
    }
    {
        PyObject *tmp_called_value_6;
        PyObject *tmp_call_result_6;
        PyObject *tmp_args_element_value_2;
        PyObject *tmp_args_element_value_3;
        tmp_called_value_6 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_6 != NULL);
        tmp_args_element_value_2 = mod_consts[21];
        tmp_args_element_value_3 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[19]);

        if (unlikely(tmp_args_element_value_3 == NULL)) {
            tmp_args_element_value_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[19]);
        }

        assert(!(tmp_args_element_value_3 == NULL));
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 143;
        {
            PyObject *call_args[] = {tmp_args_element_value_2, tmp_args_element_value_3};
            tmp_call_result_6 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_6, call_args);
        }

        if (tmp_call_result_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 143;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_6);
    }
    {
        PyObject *tmp_called_value_7;
        PyObject *tmp_call_result_7;
        tmp_called_value_7 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_7 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 144;
        tmp_call_result_7 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_7, mod_consts[22]);

        if (tmp_call_result_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 144;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_7);
    }
    {
        PyObject *tmp_called_value_8;
        PyObject *tmp_call_result_8;
        tmp_called_value_8 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_8 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 145;
        tmp_call_result_8 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_8, mod_consts[20]);

        if (tmp_call_result_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 145;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_8);
    }
    {
        PyObject *tmp_called_value_9;
        PyObject *tmp_call_result_9;
        tmp_called_value_9 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_9 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 146;
        tmp_call_result_9 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_9, mod_consts[20]);

        if (tmp_call_result_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 146;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_9);
    }
    {
        PyObject *tmp_called_value_10;
        PyObject *tmp_call_result_10;
        tmp_called_value_10 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_10 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 147;
        tmp_call_result_10 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_10);
        if (tmp_call_result_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 147;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_10);
    }
    {
        PyObject *tmp_called_value_11;
        PyObject *tmp_call_result_11;
        tmp_called_value_11 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_11 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 148;
        tmp_call_result_11 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_11, mod_consts[23]);

        if (tmp_call_result_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_11);
    }
    {
        PyObject *tmp_called_value_12;
        PyObject *tmp_call_result_12;
        tmp_called_value_12 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_12 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 149;
        tmp_call_result_12 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_12);
        if (tmp_call_result_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 149;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_12);
    }
    {
        PyObject *tmp_called_value_13;
        PyObject *tmp_call_result_13;
        tmp_called_value_13 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_13 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 150;
        tmp_call_result_13 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_13, mod_consts[24]);

        if (tmp_call_result_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 150;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_13);
    }
    {
        PyObject *tmp_called_value_14;
        PyObject *tmp_call_result_14;
        tmp_called_value_14 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_14 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 151;
        tmp_call_result_14 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_14, mod_consts[25]);

        if (tmp_call_result_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 151;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_14);
    }
    {
        PyObject *tmp_called_value_15;
        PyObject *tmp_call_result_15;
        tmp_called_value_15 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_15 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 152;
        tmp_call_result_15 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_15);
        if (tmp_call_result_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 152;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_15);
    }
    {
        PyObject *tmp_assign_source_13;
        PyObject *tmp_int_arg_1;
        PyObject *tmp_input_arg_2;
        tmp_input_arg_2 = mod_consts[26];
        tmp_int_arg_1 = BUILTIN_INPUT(tstate, tmp_input_arg_2);
        if (tmp_int_arg_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 153;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_13 = PyNumber_Int(tmp_int_arg_1);
        Py_DECREF(tmp_int_arg_1);
        if (tmp_assign_source_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 153;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[27], tmp_assign_source_13);
    }
    {
        PyObject *tmp_called_value_16;
        PyObject *tmp_call_result_16;
        tmp_called_value_16 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_16 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 154;
        tmp_call_result_16 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_16);
        if (tmp_call_result_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 154;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_16);
    }
    {
        nuitka_bool tmp_condition_result_2;
        PyObject *tmp_cmp_expr_left_1;
        PyObject *tmp_cmp_expr_right_1;
        tmp_cmp_expr_left_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[27]);

        if (unlikely(tmp_cmp_expr_left_1 == NULL)) {
            tmp_cmp_expr_left_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[27]);
        }

        assert(!(tmp_cmp_expr_left_1 == NULL));
        tmp_cmp_expr_right_1 = mod_consts[28];
        tmp_condition_result_2 = RICH_COMPARE_EQ_NBOOL_OBJECT_LONG(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
        if (tmp_condition_result_2 == NUITKA_BOOL_EXCEPTION) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 155;

            goto frame_exception_exit_1;
        }
        if (tmp_condition_result_2 == NUITKA_BOOL_TRUE) {
            goto branch_yes_2;
        } else {
            goto branch_no_2;
        }
    }
    branch_yes_2:;
    {
        PyObject *tmp_called_value_17;
        PyObject *tmp_call_result_17;
        tmp_called_value_17 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_17 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 156;
        tmp_call_result_17 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_17, mod_consts[20]);

        if (tmp_call_result_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 156;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_17);
    }
    {
        PyObject *tmp_called_value_18;
        PyObject *tmp_call_result_18;
        tmp_called_value_18 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_18 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 157;
        tmp_call_result_18 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_18, mod_consts[29]);

        if (tmp_call_result_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 157;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_18);
    }
    {
        PyObject *tmp_called_value_19;
        PyObject *tmp_call_result_19;
        tmp_called_value_19 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_19 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 158;
        tmp_call_result_19 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_19, mod_consts[20]);

        if (tmp_call_result_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 158;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_19);
    }
    {
        PyObject *tmp_called_value_20;
        PyObject *tmp_call_result_20;
        tmp_called_value_20 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_20 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 159;
        tmp_call_result_20 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_20);
        if (tmp_call_result_20 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 159;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_20);
    }
    {
        PyObject *tmp_assign_source_14;
        PyObject *tmp_iter_arg_1;
        tmp_iter_arg_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[10]);

        if (unlikely(tmp_iter_arg_1 == NULL)) {
            tmp_iter_arg_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[10]);
        }

        if (tmp_iter_arg_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 160;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_14 = MAKE_ITERATOR(tstate, tmp_iter_arg_1);
        if (tmp_assign_source_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 160;

            goto frame_exception_exit_1;
        }
        {
            PyObject *old = tmp_for_loop_1__for_iterator;
            tmp_for_loop_1__for_iterator = tmp_assign_source_14;
            Py_XDECREF(old);
        }

    }
    // Tried code:
    loop_start_2:;
    {
        PyObject *tmp_next_source_1;
        PyObject *tmp_assign_source_15;
        CHECK_OBJECT(tmp_for_loop_1__for_iterator);
        tmp_next_source_1 = tmp_for_loop_1__for_iterator;
        tmp_assign_source_15 = ITERATOR_NEXT(tmp_next_source_1);
        if (tmp_assign_source_15 == NULL) {
            if (CHECK_AND_CLEAR_STOP_ITERATION_OCCURRED(tstate)) {

                goto loop_end_2;
            } else {

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);

                exception_lineno = 160;
                goto try_except_handler_1;
            }
        }

        {
            PyObject *old = tmp_for_loop_1__iter_value;
            tmp_for_loop_1__iter_value = tmp_assign_source_15;
            Py_XDECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_16;
        CHECK_OBJECT(tmp_for_loop_1__iter_value);
        tmp_assign_source_16 = tmp_for_loop_1__iter_value;
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[30], tmp_assign_source_16);
    }
    {
        PyObject *tmp_assign_source_17;
        PyObject *tmp_called_value_21;
        PyObject *tmp_expression_value_2;
        tmp_expression_value_2 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[30]);

        if (unlikely(tmp_expression_value_2 == NULL)) {
            tmp_expression_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[30]);
        }

        assert(!(tmp_expression_value_2 == NULL));
        tmp_called_value_21 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_2, mod_consts[31]);
        if (tmp_called_value_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 161;

            goto try_except_handler_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 161;
        tmp_assign_source_17 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_21, mod_consts[32]);

        Py_DECREF(tmp_called_value_21);
        if (tmp_assign_source_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 161;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[33], tmp_assign_source_17);
    }
    {
        PyObject *tmp_called_value_22;
        PyObject *tmp_call_result_21;
        PyObject *tmp_args_element_value_4;
        tmp_called_value_22 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_22 != NULL);
        tmp_args_element_value_4 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[33]);

        if (unlikely(tmp_args_element_value_4 == NULL)) {
            tmp_args_element_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[33]);
        }

        assert(!(tmp_args_element_value_4 == NULL));
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 162;
        tmp_call_result_21 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_22, tmp_args_element_value_4);
        if (tmp_call_result_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 162;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_21);
    }
    {
        PyObject *tmp_called_value_23;
        PyObject *tmp_call_result_22;
        tmp_called_value_23 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_23 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 163;
        tmp_call_result_22 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_23);
        if (tmp_call_result_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 163;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_22);
    }
    {
        PyObject *tmp_assign_source_18;
        PyObject *tmp_str_arg_value_1;
        PyObject *tmp_input_arg_3;
        tmp_input_arg_3 = mod_consts[34];
        tmp_str_arg_value_1 = BUILTIN_INPUT(tstate, tmp_input_arg_3);
        if (tmp_str_arg_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 164;

            goto try_except_handler_1;
        }
        tmp_assign_source_18 = UNICODE_UPPER(tstate, tmp_str_arg_value_1);
        Py_DECREF(tmp_str_arg_value_1);
        if (tmp_assign_source_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 164;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[35], tmp_assign_source_18);
    }
    {
        PyObject *tmp_called_value_24;
        PyObject *tmp_call_result_23;
        tmp_called_value_24 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_24 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 165;
        tmp_call_result_23 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_24);
        if (tmp_call_result_23 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 165;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_23);
    }
    {
        PyObject *tmp_assign_source_19;
        PyObject *tmp_called_value_25;
        PyObject *tmp_expression_value_3;
        tmp_expression_value_3 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[30]);

        if (unlikely(tmp_expression_value_3 == NULL)) {
            tmp_expression_value_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[30]);
        }

        if (tmp_expression_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 166;

            goto try_except_handler_1;
        }
        tmp_called_value_25 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_3, mod_consts[31]);
        if (tmp_called_value_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 166;

            goto try_except_handler_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 166;
        tmp_assign_source_19 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_25, mod_consts[36]);

        Py_DECREF(tmp_called_value_25);
        if (tmp_assign_source_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 166;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[37], tmp_assign_source_19);
    }
    {
        nuitka_bool tmp_condition_result_3;
        PyObject *tmp_cmp_expr_left_2;
        PyObject *tmp_cmp_expr_right_2;
        tmp_cmp_expr_left_2 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[35]);

        if (unlikely(tmp_cmp_expr_left_2 == NULL)) {
            tmp_cmp_expr_left_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[35]);
        }

        if (tmp_cmp_expr_left_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 167;

            goto try_except_handler_1;
        }
        tmp_cmp_expr_right_2 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[37]);

        if (unlikely(tmp_cmp_expr_right_2 == NULL)) {
            tmp_cmp_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[37]);
        }

        assert(!(tmp_cmp_expr_right_2 == NULL));
        tmp_condition_result_3 = RICH_COMPARE_EQ_NBOOL_OBJECT_OBJECT(tmp_cmp_expr_left_2, tmp_cmp_expr_right_2);
        if (tmp_condition_result_3 == NUITKA_BOOL_EXCEPTION) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 167;

            goto try_except_handler_1;
        }
        if (tmp_condition_result_3 == NUITKA_BOOL_TRUE) {
            goto branch_yes_3;
        } else {
            goto branch_no_3;
        }
    }
    branch_yes_3:;
    {
        PyObject *tmp_called_value_26;
        PyObject *tmp_call_result_24;
        tmp_called_value_26 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_26 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 168;
        tmp_call_result_24 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_26, mod_consts[38]);

        if (tmp_call_result_24 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 168;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_24);
    }
    {
        PyObject *tmp_assign_source_20;
        PyObject *tmp_iadd_expr_left_1;
        PyObject *tmp_iadd_expr_right_1;
        tmp_iadd_expr_left_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_iadd_expr_left_1 == NULL)) {
            tmp_iadd_expr_left_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[14]);
        }

        if (tmp_iadd_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 169;

            goto try_except_handler_1;
        }
        tmp_iadd_expr_right_1 = mod_consts[39];
        tmp_inplace_orig = tmp_iadd_expr_left_1;
        tmp_result = INPLACE_OPERATION_ADD_OBJECT_LONG(&tmp_iadd_expr_left_1, tmp_iadd_expr_right_1);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 169;

            goto try_except_handler_1;
        }
        tmp_assign_source_20 = tmp_iadd_expr_left_1;
        if (tmp_inplace_orig != tmp_assign_source_20) {
            UPDATE_STRING_DICT_INPLACE(moduledict___main__, (Nuitka_StringObject *)mod_consts[14], tmp_assign_source_20);
        }
    }
    {
        PyObject *tmp_called_value_27;
        PyObject *tmp_call_result_25;
        PyObject *tmp_args_element_value_5;
        PyObject *tmp_add_expr_left_1;
        PyObject *tmp_add_expr_right_1;
        PyObject *tmp_args_element_value_6;
        tmp_called_value_27 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_27 != NULL);
        tmp_add_expr_left_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[19]);

        if (unlikely(tmp_add_expr_left_1 == NULL)) {
            tmp_add_expr_left_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[19]);
        }

        if (tmp_add_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 170;

            goto try_except_handler_1;
        }
        tmp_add_expr_right_1 = mod_consts[40];
        tmp_args_element_value_5 = BINARY_OPERATION_ADD_OBJECT_OBJECT_UNICODE(tmp_add_expr_left_1, tmp_add_expr_right_1);
        if (tmp_args_element_value_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 170;

            goto try_except_handler_1;
        }
        tmp_args_element_value_6 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_args_element_value_6 == NULL)) {
            tmp_args_element_value_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[14]);
        }

        if (tmp_args_element_value_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_args_element_value_5);

            exception_lineno = 170;

            goto try_except_handler_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 170;
        {
            PyObject *call_args[] = {tmp_args_element_value_5, tmp_args_element_value_6};
            tmp_call_result_25 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_27, call_args);
        }

        Py_DECREF(tmp_args_element_value_5);
        if (tmp_call_result_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 170;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_25);
    }
    {
        PyObject *tmp_called_value_28;
        PyObject *tmp_call_result_26;
        PyObject *tmp_args_element_value_7;
        PyObject *tmp_args_element_value_8;
        tmp_called_value_28 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_28 != NULL);
        tmp_args_element_value_7 = mod_consts[41];
        tmp_args_element_value_8 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_args_element_value_8 == NULL)) {
            tmp_args_element_value_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[13]);
        }

        if (tmp_args_element_value_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 171;

            goto try_except_handler_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 171;
        {
            PyObject *call_args[] = {tmp_args_element_value_7, tmp_args_element_value_8};
            tmp_call_result_26 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_28, call_args);
        }

        if (tmp_call_result_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 171;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_26);
    }
    {
        PyObject *tmp_called_value_29;
        PyObject *tmp_call_result_27;
        tmp_called_value_29 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_29 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 172;
        tmp_call_result_27 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_29);
        if (tmp_call_result_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 172;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_27);
    }
    {
        PyObject *tmp_called_value_30;
        PyObject *tmp_call_result_28;
        tmp_called_value_30 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_30 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 173;
        tmp_call_result_28 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_30, mod_consts[20]);

        if (tmp_call_result_28 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 173;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_28);
    }
    {
        PyObject *tmp_called_value_31;
        PyObject *tmp_call_result_29;
        tmp_called_value_31 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_31 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 174;
        tmp_call_result_29 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_31);
        if (tmp_call_result_29 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 174;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_29);
    }
    goto branch_end_3;
    branch_no_3:;
    {
        PyObject *tmp_called_value_32;
        PyObject *tmp_call_result_30;
        PyObject *tmp_args_element_value_9;
        PyObject *tmp_args_element_value_10;
        tmp_called_value_32 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_32 != NULL);
        tmp_args_element_value_9 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[35]);

        if (unlikely(tmp_args_element_value_9 == NULL)) {
            tmp_args_element_value_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[35]);
        }

        if (tmp_args_element_value_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 176;

            goto try_except_handler_1;
        }
        tmp_args_element_value_10 = mod_consts[42];
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 176;
        {
            PyObject *call_args[] = {tmp_args_element_value_9, tmp_args_element_value_10};
            tmp_call_result_30 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_32, call_args);
        }

        if (tmp_call_result_30 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 176;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_30);
    }
    {
        PyObject *tmp_called_value_33;
        PyObject *tmp_call_result_31;
        PyObject *tmp_args_element_value_11;
        PyObject *tmp_args_element_value_12;
        tmp_called_value_33 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_33 != NULL);
        tmp_args_element_value_11 = mod_consts[43];
        tmp_args_element_value_12 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[37]);

        if (unlikely(tmp_args_element_value_12 == NULL)) {
            tmp_args_element_value_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[37]);
        }

        if (tmp_args_element_value_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 177;
        {
            PyObject *call_args[] = {tmp_args_element_value_11, tmp_args_element_value_12};
            tmp_call_result_31 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_33, call_args);
        }

        if (tmp_call_result_31 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_31);
    }
    {
        PyObject *tmp_called_value_34;
        PyObject *tmp_call_result_32;
        PyObject *tmp_args_element_value_13;
        PyObject *tmp_add_expr_left_2;
        PyObject *tmp_add_expr_right_2;
        PyObject *tmp_args_element_value_14;
        tmp_called_value_34 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_34 != NULL);
        tmp_add_expr_left_2 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[19]);

        if (unlikely(tmp_add_expr_left_2 == NULL)) {
            tmp_add_expr_left_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[19]);
        }

        if (tmp_add_expr_left_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 178;

            goto try_except_handler_1;
        }
        tmp_add_expr_right_2 = mod_consts[40];
        tmp_args_element_value_13 = BINARY_OPERATION_ADD_OBJECT_OBJECT_UNICODE(tmp_add_expr_left_2, tmp_add_expr_right_2);
        if (tmp_args_element_value_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 178;

            goto try_except_handler_1;
        }
        tmp_args_element_value_14 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_args_element_value_14 == NULL)) {
            tmp_args_element_value_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[14]);
        }

        if (tmp_args_element_value_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_args_element_value_13);

            exception_lineno = 178;

            goto try_except_handler_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 178;
        {
            PyObject *call_args[] = {tmp_args_element_value_13, tmp_args_element_value_14};
            tmp_call_result_32 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_34, call_args);
        }

        Py_DECREF(tmp_args_element_value_13);
        if (tmp_call_result_32 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 178;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_32);
    }
    {
        PyObject *tmp_assign_source_21;
        PyObject *tmp_isub_expr_left_1;
        PyObject *tmp_isub_expr_right_1;
        tmp_isub_expr_left_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_isub_expr_left_1 == NULL)) {
            tmp_isub_expr_left_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[13]);
        }

        if (tmp_isub_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 179;

            goto try_except_handler_1;
        }
        tmp_isub_expr_right_1 = mod_consts[28];
        tmp_inplace_orig = tmp_isub_expr_left_1;
        tmp_result = INPLACE_OPERATION_SUB_OBJECT_LONG(&tmp_isub_expr_left_1, tmp_isub_expr_right_1);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 179;

            goto try_except_handler_1;
        }
        tmp_assign_source_21 = tmp_isub_expr_left_1;
        if (tmp_inplace_orig != tmp_assign_source_21) {
            UPDATE_STRING_DICT_INPLACE(moduledict___main__, (Nuitka_StringObject *)mod_consts[13], tmp_assign_source_21);
        }
    }
    {
        PyObject *tmp_called_value_35;
        PyObject *tmp_call_result_33;
        PyObject *tmp_args_element_value_15;
        PyObject *tmp_args_element_value_16;
        tmp_called_value_35 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_35 != NULL);
        tmp_args_element_value_15 = mod_consts[41];
        tmp_args_element_value_16 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_args_element_value_16 == NULL)) {
            tmp_args_element_value_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[13]);
        }

        assert(!(tmp_args_element_value_16 == NULL));
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 180;
        {
            PyObject *call_args[] = {tmp_args_element_value_15, tmp_args_element_value_16};
            tmp_call_result_33 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_35, call_args);
        }

        if (tmp_call_result_33 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 180;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_33);
    }
    {
        PyObject *tmp_called_value_36;
        PyObject *tmp_call_result_34;
        tmp_called_value_36 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_36 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 181;
        tmp_call_result_34 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_36);
        if (tmp_call_result_34 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 181;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_34);
    }
    {
        PyObject *tmp_called_value_37;
        PyObject *tmp_call_result_35;
        tmp_called_value_37 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_37 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 182;
        tmp_call_result_35 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_37, mod_consts[20]);

        if (tmp_call_result_35 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 182;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_35);
    }
    {
        PyObject *tmp_called_value_38;
        PyObject *tmp_call_result_36;
        tmp_called_value_38 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_38 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 183;
        tmp_call_result_36 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_38);
        if (tmp_call_result_36 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 183;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_36);
    }
    branch_end_3:;
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_call_result_37;
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[7]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[7]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 184;

            goto try_except_handler_1;
        }
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 184;
        tmp_call_result_37 = CALL_METHOD_WITH_SINGLE_ARG(
            tstate,
            tmp_called_instance_1,
            mod_consts[44],
            PyTuple_GET_ITEM(mod_consts[45], 0)
        );

        if (tmp_call_result_37 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 184;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_37);
    }
    {
        nuitka_bool tmp_condition_result_4;
        PyObject *tmp_cmp_expr_left_3;
        PyObject *tmp_cmp_expr_right_3;
        tmp_cmp_expr_left_3 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_cmp_expr_left_3 == NULL)) {
            tmp_cmp_expr_left_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[13]);
        }

        if (tmp_cmp_expr_left_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 185;

            goto try_except_handler_1;
        }
        tmp_cmp_expr_right_3 = mod_consts[6];
        tmp_condition_result_4 = RICH_COMPARE_EQ_NBOOL_OBJECT_LONG(tmp_cmp_expr_left_3, tmp_cmp_expr_right_3);
        if (tmp_condition_result_4 == NUITKA_BOOL_EXCEPTION) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 185;

            goto try_except_handler_1;
        }
        if (tmp_condition_result_4 == NUITKA_BOOL_TRUE) {
            goto branch_yes_4;
        } else {
            goto branch_no_4;
        }
    }
    branch_yes_4:;
    {
        PyObject *tmp_called_value_39;
        PyObject *tmp_call_result_38;
        tmp_called_value_39 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_39 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 186;
        tmp_call_result_38 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_39, mod_consts[46]);

        if (tmp_call_result_38 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 186;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_38);
    }
    {
        PyObject *tmp_called_value_40;
        PyObject *tmp_call_result_39;
        tmp_called_value_40 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_40 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 187;
        tmp_call_result_39 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_40);
        if (tmp_call_result_39 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 187;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_39);
    }
    goto branch_end_4;
    branch_no_4:;
    {
        nuitka_bool tmp_condition_result_5;
        PyObject *tmp_cmp_expr_left_4;
        PyObject *tmp_cmp_expr_right_4;
        tmp_cmp_expr_left_4 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_cmp_expr_left_4 == NULL)) {
            tmp_cmp_expr_left_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[14]);
        }

        if (tmp_cmp_expr_left_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 188;

            goto try_except_handler_1;
        }
        tmp_cmp_expr_right_4 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[16]);

        if (unlikely(tmp_cmp_expr_right_4 == NULL)) {
            tmp_cmp_expr_right_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[16]);
        }

        if (tmp_cmp_expr_right_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 188;

            goto try_except_handler_1;
        }
        tmp_condition_result_5 = RICH_COMPARE_EQ_NBOOL_OBJECT_OBJECT(tmp_cmp_expr_left_4, tmp_cmp_expr_right_4);
        if (tmp_condition_result_5 == NUITKA_BOOL_EXCEPTION) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 188;

            goto try_except_handler_1;
        }
        if (tmp_condition_result_5 == NUITKA_BOOL_TRUE) {
            goto branch_yes_5;
        } else {
            goto branch_no_5;
        }
    }
    branch_yes_5:;
    {
        PyObject *tmp_called_value_41;
        PyObject *tmp_call_result_40;
        tmp_called_value_41 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_41 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 189;
        tmp_call_result_40 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_41, mod_consts[47]);

        if (tmp_call_result_40 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 189;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_40);
    }
    {
        PyObject *tmp_called_value_42;
        PyObject *tmp_call_result_41;
        tmp_called_value_42 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_42 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 190;
        tmp_call_result_41 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_42, mod_consts[47]);

        if (tmp_call_result_41 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 190;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_41);
    }
    {
        PyObject *tmp_called_value_43;
        PyObject *tmp_call_result_42;
        tmp_called_value_43 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_43 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 191;
        tmp_call_result_42 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_43, mod_consts[48]);

        if (tmp_call_result_42 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 191;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_42);
    }
    {
        PyObject *tmp_called_value_44;
        PyObject *tmp_call_result_43;
        tmp_called_value_44 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_44 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 192;
        tmp_call_result_43 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_44, mod_consts[47]);

        if (tmp_call_result_43 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 192;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_43);
    }
    {
        PyObject *tmp_called_value_45;
        PyObject *tmp_call_result_44;
        tmp_called_value_45 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_45 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 193;
        tmp_call_result_44 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_45, mod_consts[47]);

        if (tmp_call_result_44 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 193;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_44);
    }
    {
        PyObject *tmp_called_value_46;
        PyObject *tmp_call_result_45;
        tmp_called_value_46 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_46 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 194;
        tmp_call_result_45 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_46);
        if (tmp_call_result_45 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 194;

            goto try_except_handler_1;
        }
        Py_DECREF(tmp_call_result_45);
    }
    goto loop_end_2;
    branch_no_5:;
    branch_end_4:;
    if (CONSIDER_THREADING(tstate) == false) {
        assert(HAS_ERROR_OCCURRED(tstate));

        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


        exception_lineno = 160;

        goto try_except_handler_1;
    }
    goto loop_start_2;
    loop_end_2:;
    goto try_end_1;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_for_loop_1__iter_value);
    tmp_for_loop_1__iter_value = NULL;
    CHECK_OBJECT(tmp_for_loop_1__for_iterator);
    Py_DECREF(tmp_for_loop_1__for_iterator);
    tmp_for_loop_1__for_iterator = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    Py_XDECREF(tmp_for_loop_1__iter_value);
    tmp_for_loop_1__iter_value = NULL;
    CHECK_OBJECT(tmp_for_loop_1__for_iterator);
    Py_DECREF(tmp_for_loop_1__for_iterator);
    tmp_for_loop_1__for_iterator = NULL;
    goto branch_end_2;
    branch_no_2:;
    goto loop_end_1;
    branch_end_2:;
    {
        PyObject *tmp_assign_source_22;
        PyObject *tmp_input_arg_4;
        tmp_input_arg_4 = mod_consts[49];
        tmp_assign_source_22 = BUILTIN_INPUT(tstate, tmp_input_arg_4);
        if (tmp_assign_source_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 198;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict___main__, (Nuitka_StringObject *)mod_consts[50], tmp_assign_source_22);
    }
    {
        bool tmp_condition_result_6;
        PyObject *tmp_cmp_expr_left_5;
        PyObject *tmp_cmp_expr_right_5;
        tmp_cmp_expr_left_5 = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)mod_consts[50]);

        if (unlikely(tmp_cmp_expr_left_5 == NULL)) {
            tmp_cmp_expr_left_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[50]);
        }

        assert(!(tmp_cmp_expr_left_5 == NULL));
        tmp_cmp_expr_right_5 = mod_consts[51];
        tmp_condition_result_6 = RICH_COMPARE_EQ_CBOOL_UNICODE_UNICODE(tmp_cmp_expr_left_5, tmp_cmp_expr_right_5);
        if (tmp_condition_result_6 != false) {
            goto branch_yes_6;
        } else {
            goto branch_no_6;
        }
    }
    branch_yes_6:;
    {
        PyObject *tmp_assign_source_23;
        tmp_assign_source_23 = Py_False;
        UPDATE_STRING_DICT0(moduledict___main__, (Nuitka_StringObject *)mod_consts[8], tmp_assign_source_23);
    }
    {
        PyObject *tmp_called_value_47;
        PyObject *tmp_call_result_46;
        tmp_called_value_47 = LOOKUP_BUILTIN(mod_consts[17]);
        assert(tmp_called_value_47 != NULL);
        frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame.f_lineno = 201;
        tmp_call_result_46 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_47);
        if (tmp_call_result_46 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 201;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_46);
    }
    branch_no_6:;
    if (CONSIDER_THREADING(tstate) == false) {
        assert(HAS_ERROR_OCCURRED(tstate));

        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


        exception_lineno = 134;

        goto frame_exception_exit_1;
    }
    goto loop_start_1;
    loop_end_1:;


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_e684cc165ccdfe28d115fd98d1c72d0a, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_e684cc165ccdfe28d115fd98d1c72d0a->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_e684cc165ccdfe28d115fd98d1c72d0a, exception_lineno);
    }



    assertFrameObject(frame_e684cc165ccdfe28d115fd98d1c72d0a);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("__main__", false);

    Py_INCREF(module___main__);
    return module___main__;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 1
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(tstate, module_name);
        }
    }
#endif
    PGO_onModuleExit("__main__", false);

    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);
    return NULL;
}
