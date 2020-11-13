sys.stdout = io.StringIO()
self.assertEqual(mastermind.check_correctness(5, False, 4), True)
self.assertEqual(sys.stdout.getvalue(), "Congratulations! You are a codebreaker!\n")


        # self.assertFalse(mastermind.check_correctness,(1 , 3))
        # self.assertFalse(mastermind.check_correctness,(1 , 2))
        # self.assertFalse(mastermind.check_correctness,(1 , 1))
        # self.assertFalse(mastermind.check_correctness,(1 , 0))
