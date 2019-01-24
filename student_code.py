import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        #first check if new item is a fact
        #then check if fact is in base
        #add fact to end of list s.append(list1)

        #for the string
        #if factq(this new fact) = true
        #nest another if this fact if ____ in thislist then exit
        #newfact.append(thelist)

        if factq(fact.name):
            if fact in self.facts:
                return
            else:
                self.facts.append(fact)
        else:
            return

        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):

        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        #if the fact is a fact and is in self.facts, return ListofBindings (from match) or return False if fact isn't in facts
        #go through whole list even if binding is found

        x = ListOfBindings()
        #b = Bindings()

        #if factq(fact.name):
        for y in self.facts:
            a = match(y.statement, fact.statement)
            if a == False:
                continue
            else:
                x.add_bindings(a, fact.statement)
        return x


       # else:
           # return False
        #else:
         #   return

        print("Asking {!r}".format(fact))
