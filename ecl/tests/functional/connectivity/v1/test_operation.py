# -*- coding: utf-8 -*-


import six

from ecl.tests.functional import base


class TestOperation(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestOperation, cls).setUpClass()
        mcics = list(cls.conn.connectivity.mcics())
        cls.one_mcic = None
        cls.one_operation = None
        cls.one_cic = None
        if mcics and len(mcics) > 0:
            cls.one_mcic = mcics[0]
        if cls.one_mcic is not None:
            cics = list(cls.conn.connectivity.cics(cls.one_mcic.mcic_id))
            if cics and len(cics) > 0:
                cls.one_cic = cics[0]
            operations = list(cls.conn.connectivity.operations(mcic_id=cls.one_mcic.mcic_id))
            if operations and len(operations) > 0:
                cls.one_operation = operations[0]

    def test_operations_by_mcic(self):
        if self.one_mcic is None:
            return
        operations = list(self.conn.connectivity.operations(self.one_mcic.mcic_id))
        self.assertGreaterEqual(len(operations), 0)

        for operation in operations:
            # print(operation.to_dict()["mcic_id"])
            self.assertIsInstance(operation.operation_id, six.string_types)
            self.assertIsInstance(operation.operation_status, six.string_types)
            self.assertIsInstance(operation.operation_type, six.string_types)
            self.assertIsInstance(operation.operation_body, dict)
            self.assertEqual(operation.mcic_id, self.one_mcic.mcic_id)
            self.assertIsInstance(operation.user_id, six.string_types)
            self.assertIsInstance(operation.user_name, six.string_types)
            if operation.reciept_date:
                self.assertIsInstance(operation.reciept_date, six.string_types)
            self.assertIsInstance(operation.error_messages, list)

    def test_operations_by_cic(self):
        if self.one_cic is None:
            return
        cic_operations = self.conn.connectivity.operations(cic_id=self.one_cic.cic_id)
        for operation in cic_operations:
            # print(operation.to_dict()["cic_id"])
            self.assertIsInstance(operation.operation_id, six.string_types)
            self.assertIsInstance(operation.operation_status, six.string_types)
            self.assertIsInstance(operation.operation_type, six.string_types)
            self.assertIsInstance(operation.operation_body, dict)
            self.assertEqual(operation.cic_id, self.one_cic.cic_id)
            self.assertIsInstance(operation.user_id, six.string_types)
            self.assertIsInstance(operation.user_name, six.string_types)
            if operation.reciept_date:
                self.assertIsInstance(operation.reciept_date, six.string_types)
            self.assertIsInstance(operation.error_messages, list)

    def test_get_operation_by_id(self):
        if self.one_operation is None:
            return
        operation = self.conn.connectivity.get_operation(self.one_operation.operation_id)
        # print(operation.to_dict())
        self.assertEqual(operation.operation_id, self.one_operation.operation_id)
        self.assertEqual(operation.operation_status, self.one_operation.operation_status)
        self.assertEqual(operation.operation_type, self.one_operation.operation_type)
        self.assertEqual(operation.operation_body, self.one_operation.operation_body)
        self.assertEqual(operation.user_id, self.one_operation.user_id)
        self.assertEqual(operation.user_name, self.one_operation.user_name)
        self.assertEqual(operation.reciept_date, self.one_operation.reciept_date)
        self.assertEqual(operation.error_messages, self.one_operation.error_messages)
