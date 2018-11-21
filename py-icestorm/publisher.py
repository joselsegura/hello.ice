#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import sys
import Ice
import IceStorm
import time
Ice.loadSlice('./Printer.ice')
import Example


class Publisher(Ice.Application):
    def get_topic_manager(self):
        key = 'IceStorm.TopicManager.Proxy'
        proxy = self.communicator().propertyToProxy(key)
        if proxy is None:
            print "property", key, "not set"
            return None

        print("Using IceStorm in: '%s'" % key)
        return IceStorm.TopicManagerPrx.checkedCast(proxy)

    def run(self, argv):
        topic_mgr = self.get_topic_manager()
        if not topic_mgr:
            print(': invalid proxy')
            return 2

        topic_name = "PrinterTopic"
        try:
            topic = topic_mgr.retrieve(topic_name)
        except IceStorm.NoSuchTopic:
            print("Topic {} not found, creating...".format(topic_name))
            topic = topic_mgr.create(topic_name)

        publisher = topic.getPublisher()
        printer = Example.PrinterPrx.uncheckedCast(publisher)

        print "publishing 10 'Hello World' events"
        for i in range(100):
            printer.write("Hello World %s!" % i)
            time.sleep(1)

        return 0


sys.exit(Publisher().main(sys.argv))
