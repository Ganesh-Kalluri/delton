# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import _lt

ERROR_CODES = {
    "100": _lt("Invalid json"),
    "101": _lt("Invalid Username"),
    "102": _lt("Invalid Password"),
    "103": _lt("Invalid Client -Id"),
    "104": _lt("Invalid Client -Id"),
    "105": _lt("Invalid Token"),
    "106": _lt("Token Expired"),
    "107": _lt("Authentication failed. Pls. inform the helpdesk"),
    "108": _lt("Invalid login credentials."),
    "109": _lt("Decryption of data failed"),
    "110": _lt("Invalid Client-ID/Client-Secret"),
    "111": _lt("GSTIN is not registerd to this GSP"),
    "112": _lt("IMEI does not belong to the user"),
    "113": _lt("operating-system-type is mandatory in header"),
    "114": _lt("Invalid operating-system-type parameter value"),
    "201": _lt("Invalid Supply Type"),
    "202": _lt("Invalid Sub-supply Type"),
    "203": _lt("Sub-transaction type does not belongs to transaction type"),
    "204": _lt("Invalid Document type"),
    "205": _lt("Document type does not match with transaction & Sub trans type"),
    "206": _lt("Invaild Invoice Number"),
    "207": _lt("Invalid Invoice Date"),
    "208": _lt("Invalid Supplier GSTIN"),
    "209": _lt("Blank Supplier Address"),
    "210": _lt("Invalid or Blank Supplier PIN Code"),
    "211": _lt("Invalid or Blank Supplier state Code"),
    "212": _lt("Invalid Consignee GSTIN"),
    "213": _lt("Invalid Consignee Address"),
    "214": _lt("Invalid Consignee PIN Code"),
    "215": _lt("Invalid Consignee State Code"),
    "216": _lt("Invalid HSN Code"),
    "217": _lt("Invalid UQC Code"),
    "218": _lt("Invalid Tax Rate for Intra State Transaction"),
    "219": _lt("Invalid Tax Rate for Inter State Transaction"),
    "220": _lt("Invalid Trans mode"),
    "221": _lt("Invalid Approximate Distance"),
    "222": _lt("Invalid Transporter Id"),
    "223": _lt("Invalid Transaction Document Number"),
    "224": _lt("Invalid Transaction Date"),
    "225": _lt("Invalid Vehicle Number Format"),
    "226": _lt("Both Transaction and Vehicle Number Blank"),
    "227": _lt("User Gstin cannot be blank"),
    "228": _lt("User id cannot be blank"),
    "229": _lt("Supplier name is required"),
    "230": _lt("Supplier place is required"),
    "231": _lt("Consignee name is required"),
    "232": _lt("Consignee place is required"),
    "233": _lt("Eway bill does not contains any items"),
    "234": _lt("Total amount/Taxable amout is mandatory"),
    "235": _lt("Tax rates for Intra state transaction is blank"),
    "236": _lt("Tax rates for Inter state transaction is blank"),
    "237": _lt("Invalid client -Id/client-secret"),
    "238": _lt("Invalid auth token"),
    "239": _lt("Invalid action"),
    "240": _lt("Could not generate eway bill, pls contact helpdesk"),
    "242": _lt("Invalid or Blank Officer StateCode"),
    "243": _lt("Invalid or Blank IR Number"),
    "244": _lt("Invalid or Blank Actual Vehicle Number Format"),
    "245": _lt("Invalid Verification Date Format"),
    "246": _lt("Invalid Vehicle Release Date Format"),
    "247": _lt("Invalid Verification Time Format"),
    "248": _lt("Invalid Vehicle Release Date Format"),
    "249": _lt("Actual Value cannot be less than or equal to zero"),
    "250": _lt("Invalid Vehicle Release Date Format"),
    "251": _lt("CGST nad SGST TaxRate should be same"),
    "252": _lt("Invalid CGST Tax Rate"),
    "253": _lt("Invalid SGST Tax Rate"),
    "254": _lt("Invalid IGST Tax Rate"),
    "255": _lt("Invalid CESS Rate"),
    "256": _lt("Invalid Cess Non Advol value"),
    "278": _lt("User Gstin does not match with Transporter Id"),
    "280": _lt("Status is not ACTIVE"),
    "281": _lt("Eway Bill is already expired hence update transporter is not allowed."),
    "301": _lt("Invalid eway bill number"),
    "302": _lt("Invalid transporter mode"),
    "303": _lt("Vehicle number is required"),
    "304": _lt("Invalid vehicle format"),
    "305": _lt("Place from is required"),
    "306": _lt("Invalid from state"),
    "307": _lt("Invalid reason"),
    "308": _lt("Invalid remarks"),
    "309": _lt("Could not update vehicle details, pl contact helpdesk"),
    "311": _lt("Validity period lapsed, you cannot update vehicle details"),
    "312": _lt("This eway bill is either not generated by you or cancelled"),
    "313": _lt("Error in validating ewaybill for vehicle updation"),
    "315": _lt("Validity period lapsed, you cannot cancel this eway bill"),
    "316": _lt("Eway bill is already verified, you cannot cancel it"),
    "317": _lt("Could not cancel eway bill, please contact helpdesk"),
    "320": _lt("Invalid state to"),
    "321": _lt("Invalid place to"),
    "322": _lt("Could not generate consolidated eway bill"),
    "325": _lt("Could not retrieve data"),
    "326": _lt("Could not retrieve GSTIN details for the given GSTIN number"),
    "327": _lt("Could not retrieve data from hsn"),
    "328": _lt("Could not retrieve transporter details from gstin"),
    "329": _lt("Could not retrieve States List"),
    "330": _lt("Could not retrieve UQC list"),
    "331": _lt("Could not retrieve Error code"),
    "334": _lt("Could not retrieve user details by userid "),
    "336": _lt("Could not retrieve transporter data by gstin "),
    "337": _lt("Could not retrieve HSN details for the given HSN number"),
    "338": _lt("You cannot update transporter details, as the current tranporter is already entered Part B details of the eway bill"),
    "339": _lt("You are not assigned to update the tranporter details of this eway bill"),
    "341": _lt("This e-way bill is generated by you and hence you cannot reject it"),
    "342": _lt("You cannot reject this e-way bill as you are not the other party to do so"),
    "343": _lt("This e-way bill is cancelled"),
    "344": _lt("Invalid eway bill number"),
    "345": _lt("Validity period lapsed, you cannot reject the e-way bill"),
    "346": _lt("You can reject the e-way bill only within 72 hours from generated time"),
    "347": _lt("Validation of eway bill number failed, while rejecting ewaybill"),
    "348": _lt("Part-B is not generated for this e-way bill, hence rejection is not allowed."),
    "350": _lt("Could not generate consolidated eway bill"),
    "351": _lt("Invalid state code"),
    "352": _lt("Invalid rfid date"),
    "353": _lt("Invalid location code"),
    "354": _lt("Invalid rfid number"),
    "355": _lt("Invalid Vehicle Number Format"),
    "356": _lt("Invalid wt on bridge"),
    "357": _lt("Could not retrieve eway bill details, pl. contact helpdesk"),
    "358": _lt("GSTIN passed in request header is not matching with the user gstin mentioned in payload JSON"),
    "359": _lt("User GSTIN should match to GSTIN(from) for outward transactions"),
    "360": _lt("User GSTIN should match to GSTIN(to) for inward transactions"),
    "361": _lt("Invalid Vehicle Type"),
    "362": _lt("Transporter document date cannot be earlier than the invoice date"),
    "363": _lt("E-way bill is not enabled for intra state movement for you state"),
    "364": _lt("Error in verifying eway bill"),
    "365": _lt("Error in verifying consolidated eway bill"),
    "366": _lt("You will not get the ewaybills generated today, howerver you cann access the ewaybills of yester days"),
    "367": _lt("Could not retrieve data for officer login"),
    "368": _lt("Could not update transporter"),
    "369": _lt("GSTIN/Transin passed in request header should match with the transported Id mentioned in payload JSON"),
    "370": _lt("GSTIN/Transin passed in request header should not be the same as supplier(fromGSTIN) or recepient(toGSTIN)"),
    "371": _lt("Invalid or Blank Supplier Ship-to State Code"),
    "372": _lt("Invalid or Blank Consignee Ship-to State Code"),
    "373": _lt("The Supplier ship-to state code should be Other Country for Sub Supply Type- Export"),
    "374": _lt("The Consignee pin code should be 999999 for Sub Supply Type- Export"),
    "375": _lt("The Supplier ship-from state code should be Other Country for Sub Supply Type- Import"),
    "376": _lt("The Supplier pin code should be 999999 for Sub Supply Type- Import"),
    "377": _lt("Sub Supply Type is mentioned as Others, the description for that is mandatory"),
    "378": _lt("The supplier or conginee belong to SEZ, Inter state tax rates are applicable here"),
    "379": _lt("Eway Bill can not be extended.. Already Cancelled"),
    "380": _lt("Eway Bill Can not be Extended. Not in Active State"),
    "381": _lt("There is No PART-B/Vehicle Entry.. So Please Update Vehicle Information.."),
    "382": _lt("You Cannot Extend as EWB can be Extended only 8 hour before or after w.r.t Validity of EWB..!!"),
    "383": _lt("Error While Extending..Please Contact Helpdesk. "),
    "384": _lt("You are not current transporter or Generator of the ewayBill, with no transporter details."),
    "385": _lt("For Rail/Ship/Air transDocDate is mandatory"),
    "386": _lt("Reason Code, Remarks is mandatory."),
    "387": _lt("No Record Found for Entered consolidated eWay bill."),
    "388": _lt("Exception in regenration of consolidated eWayBill!!Please Contact helpdesk"),
    "389": _lt("Remaining Distance Required"),
    "390": _lt("Remaining Distance Can not be greater than Actual Distance."),
    "391": _lt("No eway bill of specified tripsheet, neither  ACTIVE nor not Valid."),
    "392": _lt("Tripsheet is already cancelled, Hence Regeration is not possible"),
    "393": _lt("Invalid GSTIN"),
    "394": _lt("For other than Road Transport, TransDoc number is required"),
    "395": _lt("Eway Bill Number should be numeric only"),
    "396": _lt("Either Eway Bill Number Or Consolidated Eway Bill Number is required for Verification"),
    "397": _lt("Error in Multi Vehicle Movement Initiation"),
    "398": _lt("Eway Bill Item List is Empty"),
    "399": _lt("Unit Code is not matching with any of the Unit Code from eway bill ItemList"),
    "400": _lt("total quantity is exceeding from multi vehicle movement initiation quantity"),
    "401": _lt("Error in inserting multi vehicle details"),
    "402": _lt("total quantity can not be less than or equal to zero"),
    "403": _lt("Error in multi vehicle details"),
    "405": _lt("No record found for multi vehicle update with specified ewbNo groupNo and old vehicleNo/transDocNo with status as ACT"),
    "406": _lt("Group number cannot be empty or zero"),
    "407": _lt("Invalid old vehicle number format"),
    "408": _lt("Invalid new vehicle number format"),
    "409": _lt("Invalid old transDoc number"),
    "410": _lt("Invalid new transDoc number"),
    "411": _lt("Multi Vehicle Initiation data is not there for specified ewayBill and group No"),
    "412": _lt("Multi Vehicle movement is already Initiated,hence PART B updation not allowed"),
    "413": _lt("Unit Code is not matching with unit code of first initiaton"),
    "415": _lt("Error in fetching in verification data for officer"),
    "416": _lt("Date range is exceeding allowed date range "),
    "417": _lt("No verification data found for officer "),
    "418": _lt("No record found"),
    "419": _lt("Error in fetching search result for taxpayer/transporter"),
    "420": _lt("Minimum six character required for Tradename/legalname search"),
    "421": _lt("Invalid pincode"),
    "422": _lt("Invalid mobile number"),
    "423": _lt("Error in fetching ewaybill list by vehicle number"),
    "424": _lt("Invalid PAN number"),
    "425": _lt("Error in fetching Part A data by IR Number"),
    "426": _lt("For Vehicle Released vehicle release date and time is mandatory"),
    "427": _lt("Error in saving Part-A verification Report"),
    "428": _lt("For Goods Detained,Vehicle Released feild is mandatory"),
    "429": _lt("Error in saving Part-B verification Report"),
    "430": _lt("Goods Detained Field required."),
    "431": _lt("Part-A for this ewaybill is already generated by you."),
    "432": _lt("invalid vehicle released value"),
    "433": _lt("invalid goods detained parameter value"),
    "434": _lt("invalid ewbNoAvailable parameter value"),
    "435": _lt("Part B is already updated,hence updation is not allowed"),
    "436": _lt("Invalid Consignee ship to State Code for the given pincode"),
    "437": _lt("Invalid Supplier ship from State Code for the given pincode"),
    "438": _lt("Invalid Latitude"),
    "439": _lt("Invalid Longitude"),
    "440": _lt("Error in inserting in verification data"),
    "441": _lt("Invalid verification type"),
    "442": _lt("Error in inserting verification details"),
    "443": _lt("invalid invoice available value"),
    "600": _lt("Invalid category"),
    "601": _lt("Invalid date format"),
    "602": _lt("Invalid File Number"),
    "603": _lt("For file details file number is required"),
    "604": _lt("E-way bill(s) are already generated for the same document number, you cannot generate again on same document number"),
    "607": _lt("dispatch from gstin is mandatary "),
    "608": _lt("ship to from gstin is mandatary"),
    "609": _lt(" invalid ship to from gstin "),
    "610": _lt("invalid dispatch from gstin "),
    "611": _lt("invalid document type for the given supply type "),
    "612": _lt("Invalid transaction type"),
    "613": _lt("Exception in getting Officer Role"),
    "614": _lt("Transaction type is mandatory"),
    "615": _lt("Dispatch From GSTIN cannot be sent as the transaction type selected is Regular"),
    "616": _lt("Ship to GSTIN cannot be sent as the transaction type selected is Regular"),
    "617": _lt("Bill-from and dispatch-from gstin should not be same for this transaction type"),
    "618": _lt("Bill-to and ship-to gstin should not be same for this transaction type"),
    "619": _lt("Transporter Id is mandatory for generation of Part A slip"),
    "620": _lt("Total invoice value cannot be less than the sum of total assessible value and tax values"),
    "621": _lt("Transport mode is mandatory since vehicle number is present"),
    "622": _lt("Transport mode is mandatory since transport document number is present"),
    "623": _lt("IGST value is not applicable for Intra State Transaction"),
    "624": _lt("CGST/SGST value is not applicable for Inter State Transaction"),
    "627": _lt("Total value should not be negative"),
    "628": _lt("Total invoice value should not be negative"),
    "629": _lt("IGST value should not be negative"),
    "630": _lt("CGST value should not be negative"),
    "631": _lt("SGST value should not be negative"),
    "632": _lt("Cess value should not be negative"),
    "633": _lt("Cess non advol should not be negative"),
    "634": _lt("Vehicle type should not be ODC when transmode is other than road"),
    "635": _lt("You cannot update part B, as the current tranporter is already entered Part B details of the eway bill"),
    "636": _lt("You are not assigned to update part B"),
    "637": _lt("You cannot extend ewaybill, as the current tranporter is already entered Part B details of the ewaybill"),
    "638": _lt("Transport mode is mandatory as Vehicle Number/Transport Document Number is given"),
    "640": _lt("Tolal Invoice value is mandatory"),
    "641": _lt("For outward CKD/SKD/Lots supply type, Bill To state should be as Other Country, since the  Bill To GSTIN given is of SEZ unit"),
    "642": _lt("For inward CKD/SKD/Lots supply type, Bill From state should be as Other Country, since the  Bill From GSTIN given is of SEZ unit"),
    "643": _lt("For regular transaction, Bill from state code and Dispatch from state code should be same"),
    "644": _lt("For regular transaction, Bill to state code and Ship to state code should be same"),
    "645": _lt("You cannot do multivehicle movement, as the current tranporter is already entered Part B details of the ewaybill"),
    "646": _lt("You are not assigned to do MultiVehicle Movement"),
    "647": _lt("Could not insert RFID data, pl. contact helpdisk"),
    "648": _lt("Multi Vehicle movement is already Initiated,hence generation of consolidated eway bill is not allowed"),
    "649": _lt("You cannot generate consolidated eway bill , as the current tranporter is already entered Part B details of the eway bill"),
    "650": _lt("You are not assigned to generate consolidated ewaybill"),
    "651": _lt("For Category Part-A or Part-B ewbdt is mandatory"),
    "652": _lt("For Category EWB03 procdt is mandatory"),
    "654": _lt("This GSTIN has generated a common Enrolment Number. Hence you are not allowed to generate Eway bill"),
    "655": _lt("This GSTIN has generated a common Enrolment Number. Hence you cannot mention it as a tranporter"),
    "656": _lt("This Eway Bill does not belongs to your state"),
    "657": _lt("Eway Bill Category wise details will be available after 4 days only"),
    "658": _lt("You are blocked for accesing this API as the allowed number of requests has been exceeded for this duration"),
    "659": _lt("Remarks is mandatory"),
    "670": _lt("Invalid Month Parameter"),
    "671": _lt("Invalid Year Parameter"),
    "672": _lt("User Id is mandatory"),
    "673": _lt("Error in getting officer dashboard"),
    "675": _lt("Error in getting EWB03 details by acknowledgement date range"),
    "676": _lt("Error in getting EWB Not Available List by entered date range"),
    "677": _lt("Error in getting EWB Not Available List by closed date range"),
    "678": _lt("Invalid Uniq No"),
    "679": _lt("Invalid EWB03 Ack No"),
    "680": _lt("Invalid Close Reason"),
    "681": _lt("Error in Closing EWB  Verification Data"),
    "682": _lt("No Record available to Close"),
    "683": _lt("Error in fetching WatchList Data"),
    "685": _lt("Exception in fetching dashboard data"),
    "700": _lt("You are not assigned to extend e-waybill"),
    "701": _lt("Invalid Vehicle Direction"),
    "702": _lt("The distance between the pincodes given is too high"),
    "703": _lt("Since the consignor is Composite Taxpayer, inter state transactions are not allowed"),
    "704": _lt("Since the consignor is Composite Taxpayer, Tax rates should be zero"),
    "705": _lt("Invalid transit type"),
    "706": _lt("Address Line1 is mandatory"),
    "707": _lt("Address Line2 is mandatory"),
    "708": _lt("Address Line3 is mandatory"),
    "709": _lt("Pin to pin distance is not available for the given pin codes"),
    "710": _lt("Invalid state code for the given pincode"),
    "711": _lt("Invalid consignment status for the given transmode"),
    "712": _lt("Transit Type is not required as the goods are in movement"),
    "713": _lt("Transit Address is not required as the goods are in movement"),
    "714": _lt("Document type - Tax Invoice is not allowed for composite tax payer"),
    "715": _lt("The Consignor GSTIN is blocked from e-waybill generation as Return is not filed for past 2 months"),
    "716": _lt("The Consignee GSTIN is blocked from e-waybill generation as Return is not filed for past 2 months"),
    "717": _lt("The Transporter GSTIN is blocked from e-waybill generation as Return is not filed for past 2 months"),
    "718": _lt("The User GSTIN is blocked from Transporter Updation as Return is not filed for past 2 months"),
    "719": _lt("The Transporter GSTIN is blocked from Transporter Updation as Return is not filed for past 2 months"),
    "720": _lt("E Way Bill should be generated as part of IRN generation or with reference to IRN in E Invoice System, Since Supplier is enabled for E Invoice."),
    "721": _lt("The distance between the given pincodes are not available in the system. Please provide distance."),
    "722": _lt("Consignee GSTIN is cancelled and document date is later than the  De-Registration date"),
    "724": _lt("HSN code of at least one item should be of goods to generate e-Way Bill"),
    "726": _lt("Vehicle type can not be regular when transportation mode is ship"),
    "727": _lt("This e-Way Bill does not have Oxygen items"),
    "728": _lt("You can cancel the ewaybill within 24 hours from Part B entry"),
    "801": _lt("Transporter id is not required for ewaybill for gold"),
    "802": _lt("Transporter name is not required for ewaybill for gold"),
    "803": _lt("TransDocNo is not required for ewaybill for gold"),
    "804": _lt("TransDocDate is not required for ewaybill for gold"),
    "805": _lt("Vehicle No is not required for ewaybill for gold"),
    "806": _lt("Vehicle Type is not required for ewaybill for gold"),
    "807": _lt("Transmode is mandatory for ewaybill for gold"),
    "808": _lt("Inter-State ewaybill is not allowed for gold"),
    "809": _lt("Other items are not allowed with eway bill for gold"),
    "810": _lt("Transport can not be updated for EwayBill For Gold"),
    "811": _lt("Vehicle can not be updated for EwayBill For Gold"),
    "812": _lt("ConsolidatedEWB cannot be generated for EwayBill For Gold "),
    "813": _lt("Duplicate request at the same time"),
    "814": _lt("MultiVehicleMovement cannot be initiated for EWay Bill For Gold"),
    "815": _lt("Only trans mode road is allowed for Eway Bill For Gold"),
    "816": _lt("Only transmode road is allowed for extending ewaybill for gold"),
    "817": _lt("MultiVehicleMovement cannot be initiated.Eway Bill is not in Active State"),
    "818": _lt("Validity period lapsed.Cannot generate consolidated Eway Bill"),
    "819": _lt("Ewaybill cannot be generated for the document date which is prior to 01/07/2017"),
}
