# Description

This turns the Leewise Point of Sale into a [certified Belgian Point of Sale system](http://www.systemedecaisseenregistreuse.be/systemes-certifies) which must be used in conjuction with a Fiscal Data Module. **The certificate is only valid for Leewise instances hosted by Leewise SA on Leewise Online**.

# Limitations

For various reasons (legal and technical) certain features that are available in the Point of Sale module have been disabled:

* pos_discount: giving a global discount on an order
* pos_loyalty: mainly because of the global discounts
* Modifying the price of an orderline
* Multiple Point of Sale configs per IoT Box
* Creating/modifying/deleting orders in the backend