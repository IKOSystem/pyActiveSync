########################################################################
#  Copyright (C) 2013 Sol Birnbaum
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.
########################################################################


from .code_page import code_page

class as_code_pages:
    """MS-ASWBXML code pages builder"""
    @staticmethod
    def build_as_code_pages():
        code_pages = {}

        code_pages.update({
                            0: code_page("AirSync", "airsync", 0)
                            })
        code_pages[0].add(0x05, "Sync")
        code_pages[0].add(0x06, "Responses")
        code_pages[0].add(0x07, "Add")
        code_pages[0].add(0x08, "Change")
        code_pages[0].add(0x09, "Delete")
        code_pages[0].add(0x0A, "Fetch")
        code_pages[0].add(0x0B, "SyncKey")
        code_pages[0].add(0x0C, "ClientId")
        code_pages[0].add(0x0D, "ServerId")
        code_pages[0].add(0x0E, "Status")
        code_pages[0].add(0x0F, "Collection")
        code_pages[0].add(0x10, "Class")
        code_pages[0].add(0x12, "CollectionId")
        code_pages[0].add(0x13, "GetChanges")
        code_pages[0].add(0x14, "MoreAvailable")
        code_pages[0].add(0x15, "WindowSize")
        code_pages[0].add(0x16, "Commands")
        code_pages[0].add(0x17, "Options")
        code_pages[0].add(0x18, "FilterType")
        code_pages[0].add(0x1B, "Conflict")
        code_pages[0].add(0x1C, "Collections")
        code_pages[0].add(0x1D, "ApplicationData")
        code_pages[0].add(0x1E, "DeletesAsMoves")
        code_pages[0].add(0x20, "Supported")
        code_pages[0].add(0x21, "SoftDelete")
        code_pages[0].add(0x22, "MIMESupport")
        code_pages[0].add(0x23, "MIMETruncation")
        code_pages[0].add(0x24, "Wait")
        code_pages[0].add(0x25, "Limit")
        code_pages[0].add(0x26, "Partial")
        code_pages[0].add(0x27, "ConversationMode")
        code_pages[0].add(0x28, "MaxItems")
        code_pages[0].add(0x29, "HeartbeatInterval")

        code_pages.update({
                        1 : code_page( "Contacts" , "contacts", 1 )
                        })
        code_pages[1].add(0x05, "Anniversary")
        code_pages[1].add(0x06, "AssistantName")
        code_pages[1].add(0x07, "AssistantPhoneNumber")
        code_pages[1].add(0x08, "Birthday")
        code_pages[1].add(0x0C, "Business2PhoneNumber")
        code_pages[1].add(0x0D, "BusinessAddressCity")
        code_pages[1].add(0x0E, "BusinessAddressCountry")
        code_pages[1].add(0x0F, "BusinessAddressPostalCode")
        code_pages[1].add(0x10, "BusinessAddressState")
        code_pages[1].add(0x11, "BusinessAddressStreet")
        code_pages[1].add(0x12, "BusinessFaxNumber")
        code_pages[1].add(0x13, "BusinessPhoneNumber")
        code_pages[1].add(0x14, "CarPhoneNumber")
        code_pages[1].add(0x15, "Categories")
        code_pages[1].add(0x16, "Category")
        code_pages[1].add(0x17, "Children")
        code_pages[1].add(0x18, "Child")
        code_pages[1].add(0x19, "CompanyName")
        code_pages[1].add(0x1A, "Department")
        code_pages[1].add(0x1B, "Email1Address")
        code_pages[1].add(0x1C, "Email2Address")
        code_pages[1].add(0x1D, "Email3Address")
        code_pages[1].add(0x1E, "FileAs")
        code_pages[1].add(0x1F, "FirstName")
        code_pages[1].add(0x20, "Home2PhoneNumber")
        code_pages[1].add(0x21, "HomeAddressCity")
        code_pages[1].add(0x22, "HomeAddressCountry")
        code_pages[1].add(0x23, "HomeAddressPostalCode")
        code_pages[1].add(0x24, "HomeAddressState")
        code_pages[1].add(0x25, "HomeAddressStreet")
        code_pages[1].add(0x26, "HomeFaxNumber")
        code_pages[1].add(0x27, "HomePhoneNumber")
        code_pages[1].add(0x28, "JobTitle")
        code_pages[1].add(0x29, "LastName")
        code_pages[1].add(0x2A, "MiddleName")
        code_pages[1].add(0x2B, "MobilePhoneNumber")
        code_pages[1].add(0x2C, "OfficeLocation")
        code_pages[1].add(0x2D, "OtherAddressCity")
        code_pages[1].add(0x2E, "OtherAddressCountry")
        code_pages[1].add(0x2F, "OtherAddressPostalCode")
        code_pages[1].add(0x30, "OtherAddressState")
        code_pages[1].add(0x31, "OtherAddressStreet")
        code_pages[1].add(0x32, "PagerNumber")
        code_pages[1].add(0x33, "RadioPhoneNumber")
        code_pages[1].add(0x34, "Spouse")
        code_pages[1].add(0x35, "Suffix")
        code_pages[1].add(0x36, "Title")
        code_pages[1].add(0x37, "WebPage")
        code_pages[1].add(0x38, "YomiCompanyName")
        code_pages[1].add(0x39, "YomiFirstName")
        code_pages[1].add(0x3A, "YomiLastName")
        code_pages[1].add(0x3C, "Picture")
        code_pages[1].add(0x3D, "Alias")
        code_pages[1].add(0x3E, "WeightedRank")


        # Code Page 2: Email

        code_pages.update({
                        2 : code_page( "Email" , "email", 2 )
                        })
        code_pages[2].add(0x0F, "DateReceived")
        code_pages[2].add(0x11, "DisplayTo")
        code_pages[2].add(0x12, "Importance")
        code_pages[2].add(0x13, "MessageClass")
        code_pages[2].add(0x14, "Subject")
        code_pages[2].add(0x15, "Read")
        code_pages[2].add(0x16, "To")
        code_pages[2].add(0x17, "Cc")
        code_pages[2].add(0x18, "From")
        code_pages[2].add(0x19, "ReplyTo")
        code_pages[2].add(0x1A, "AllDayEvent")
        code_pages[2].add(0x1B, "Categories")
        code_pages[2].add(0x1C, "Category")
        code_pages[2].add(0x1D, "DtStamp")
        code_pages[2].add(0x1E, "EndTime")
        code_pages[2].add(0x1F, "InstanceType")
        code_pages[2].add(0x20, "BusyStatus")
        code_pages[2].add(0x21, "Location")
        code_pages[2].add(0x22, "MeetingRequest")
        code_pages[2].add(0x23, "Organizer")
        code_pages[2].add(0x24, "RecurrenceId")
        code_pages[2].add(0x25, "Reminder")
        code_pages[2].add(0x26, "ResponseRequested")
        code_pages[2].add(0x27, "Recurrences")
        code_pages[2].add(0x28, "Recurrence")
        code_pages[2].add(0x29, "Type")
        code_pages[2].add(0x2A, "Until")
        code_pages[2].add(0x2B, "Occurrences")
        code_pages[2].add(0x2C, "Interval")
        code_pages[2].add(0x2D, "DayOfWeek")
        code_pages[2].add(0x2E, "DayOfMonth")
        code_pages[2].add(0x2F, "WeekOfMonth")
        code_pages[2].add(0x30, "MonthOfYear")
        code_pages[2].add(0x31, "StartTime")
        code_pages[2].add(0x32, "Sensitivity")
        code_pages[2].add(0x33, "TimeZone")
        code_pages[2].add(0x34, "GlobalObjId")
        code_pages[2].add(0x35, "ThreadTopic")
        code_pages[2].add(0x39, "InternetCPID")
        code_pages[2].add(0x3A, "Flag")
        code_pages[2].add(0x3B, "Status")
        code_pages[2].add(0x3C, "ContentClass")
        code_pages[2].add(0x3D, "FlagType")
        code_pages[2].add(0x3E, "CompleteTime")
        code_pages[2].add(0x3F, "DisallowNewTimeProposal")


        # Code Page 3: AirNotify
        code_pages.update({
                        3 : code_page( "AirNotify" , "airnotify", 3 )
                        })


        # Code Page 4: Calendar
        code_pages.update({
                        4 : code_page( "Calendar" , "calendar", 4 )
                        })
        code_pages[4].add(0x05, "TimeZone")
        code_pages[4].add(0x06, "AllDayEvent")
        code_pages[4].add(0x07, "Attendees")
        code_pages[4].add(0x08, "Attendee")
        code_pages[4].add(0x09, "Email")
        code_pages[4].add(0x0A, "Name")
        code_pages[4].add(0x0D, "BusyStatus")
        code_pages[4].add(0x0E, "Categories")
        code_pages[4].add(0x0F, "Category")
        code_pages[4].add(0x11, "DtStamp")
        code_pages[4].add(0x12, "EndTime")
        code_pages[4].add(0x13, "Exception")
        code_pages[4].add(0x14, "Exceptions")
        code_pages[4].add(0x15, "Deleted")
        code_pages[4].add(0x16, "ExceptionStartTime")
        code_pages[4].add(0x17, "Location")
        code_pages[4].add(0x18, "MeetingStatus")
        code_pages[4].add(0x19, "OrganizerEmail")
        code_pages[4].add(0x1A, "OrganizerName")
        code_pages[4].add(0x1B, "Recurrence")
        code_pages[4].add(0x1C, "Type")
        code_pages[4].add(0x1D, "Until")
        code_pages[4].add(0x1E, "Occurrences")
        code_pages[4].add(0x1F, "Interval")
        code_pages[4].add(0x20, "DayOfWeek")
        code_pages[4].add(0x21, "DayOfMonth")
        code_pages[4].add(0x22, "WeekOfMonth")
        code_pages[4].add(0x23, "MonthOfYear")
        code_pages[4].add(0x24, "Reminder")
        code_pages[4].add(0x25, "Sensitivity")
        code_pages[4].add(0x26, "Subject")
        code_pages[4].add(0x27, "StartTime")
        code_pages[4].add(0x28, "UID")
        code_pages[4].add(0x29, "AttendeeStatus")
        code_pages[4].add(0x2A, "AttendeeType")
        code_pages[4].add(0x33, "DisallowNewTimeProposal")
        code_pages[4].add(0x34, "ResponseRequested")
        code_pages[4].add(0x35, "AppointmentReplyTime")
        code_pages[4].add(0x36, "ResponseType")
        code_pages[4].add(0x37, "CalendarType")
        code_pages[4].add(0x38, "IsLeapMonth")
        code_pages[4].add(0x39, "FirstDayOfWeek")
        code_pages[4].add(0x3A, "OnlineMeetingConfLink")
        code_pages[4].add(0x3B, "OnlineMeetingExternalLink")


        # Code Page 5: Move
        code_pages.update({
                        5 : code_page( "Move" , "move", 5 )
                        })
        code_pages[5].add(0x05, "MoveItems")
        code_pages[5].add(0x06, "Move")
        code_pages[5].add(0x07, "SrcMsgId")
        code_pages[5].add(0x08, "SrcFldId")
        code_pages[5].add(0x09, "DstFldId")
        code_pages[5].add(0x0A, "Response")
        code_pages[5].add(0x0B, "Status")
        code_pages[5].add(0x0C, "DstMsgId")


        # Code Page 6: GetItemEstimate
        code_pages.update({
                        6 : code_page( "GetItemEstimate" , "getitemestimate", 6 )
                        })
        code_pages[6].add(0x05, "GetItemEstimate")
        code_pages[6].add(0x06, "Version")
        code_pages[6].add(0x07, "Collections")
        code_pages[6].add(0x08, "Collection")
        code_pages[6].add(0x09, "Class")
        code_pages[6].add(0x0A, "CollectionId")
        code_pages[6].add(0x0B, "DateTime")
        code_pages[6].add(0x0C, "Estimate")
        code_pages[6].add(0x0D, "Response")
        code_pages[6].add(0x0E, "Status")


        # Code Page 7: FolderHierarchy
        code_pages.update({
                        7 : code_page( "FolderHierarchy" , "folderhierarchy", 7 )
                        })
        code_pages[7].add(0x07, "DisplayName")
        code_pages[7].add(0x08, "ServerId")
        code_pages[7].add(0x09, "ParentId")
        code_pages[7].add(0x0A, "Type")
        code_pages[7].add(0x0C, "Status")
        code_pages[7].add(0x0E, "Changes")
        code_pages[7].add(0x0F, "Add")
        code_pages[7].add(0x10, "Delete")
        code_pages[7].add(0x11, "Update")
        code_pages[7].add(0x12, "SyncKey")
        code_pages[7].add(0x13, "FolderCreate")
        code_pages[7].add(0x14, "FolderDelete")
        code_pages[7].add(0x15, "FolderUpdate")
        code_pages[7].add(0x16, "FolderSync")
        code_pages[7].add(0x17, "Count")


        # Code Page 8: MeetingResponse
        code_pages.update({
                        8 : code_page( "MeetingResponse" , "meetingresponse", 8 )
                        })
        code_pages[8].add(0x05, "CalendarId")
        code_pages[8].add(0x06, "CollectionId")
        code_pages[8].add(0x07, "MeetingResponse")
        code_pages[8].add(0x08, "RequestId")
        code_pages[8].add(0x09, "Request")
        code_pages[8].add(0x0A, "Result")
        code_pages[8].add(0x0B, "Status")
        code_pages[8].add(0x0C, "UserResponse")
        code_pages[8].add(0x0E, "InstanceId")


        # Code Page 9: Tasks
        code_pages.update({
                        9 : code_page( "Tasks" , "tasks", 9 )
                        })
        code_pages[9].add(0x08, "Categories")
        code_pages[9].add(0x09, "Category")
        code_pages[9].add(0x0A, "Complete")
        code_pages[9].add(0x0B, "DateCompleted")
        code_pages[9].add(0x0C, "DueDate")
        code_pages[9].add(0x0D, "UtcDueDate")
        code_pages[9].add(0x0E, "Importance")
        code_pages[9].add(0x0F, "Recurrence")
        code_pages[9].add(0x10, "Type")
        code_pages[9].add(0x11, "Start")
        code_pages[9].add(0x12, "Until")
        code_pages[9].add(0x13, "Occurrences")
        code_pages[9].add(0x14, "Interval")
        code_pages[9].add(0x15, "DayOfMonth")
        code_pages[9].add(0x16, "DayOfWeek")
        code_pages[9].add(0x17, "WeekOfMonth")
        code_pages[9].add(0x18, "MonthOfYear")
        code_pages[9].add(0x19, "Regenerate")
        code_pages[9].add(0x1A, "DeadOccur")
        code_pages[9].add(0x1B, "ReminderSet")
        code_pages[9].add(0x1C, "ReminderTime")
        code_pages[9].add(0x1D, "Sensitivity")
        code_pages[9].add(0x1E, "StartDate")
        code_pages[9].add(0x1F, "UtcStartDate")
        code_pages[9].add(0x20, "Subject")
        code_pages[9].add(0x22, "OrdinalDate")
        code_pages[9].add(0x23, "SubOrdinalDate")
        code_pages[9].add(0x24, "CalendarType")
        code_pages[9].add(0x25, "IsLeapMonth")
        code_pages[9].add(0x26, "FirstDayOfWeek")


        # Code Page 10: ResolveRecipients
        code_pages.update({
                        10 : code_page( "ResolveRecipients" , "resolverecipients", 10 )
                        })
        code_pages[10].add(0x05, "ResolveRecipients")
        code_pages[10].add(0x06, "Response")
        code_pages[10].add(0x07, "Status")
        code_pages[10].add(0x08, "Type")
        code_pages[10].add(0x09, "Recipient")
        code_pages[10].add(0x0A, "DisplayName")
        code_pages[10].add(0x0B, "EmailAddress")
        code_pages[10].add(0x0C, "Certificates")
        code_pages[10].add(0x0D, "Certificate")
        code_pages[10].add(0x0E, "MiniCertificate")
        code_pages[10].add(0x0F, "Options")
        code_pages[10].add(0x10, "To")
        code_pages[10].add(0x11, "CertificateRetrieval")
        code_pages[10].add(0x12, "RecipientCount")
        code_pages[10].add(0x13, "MaxCertificates")
        code_pages[10].add(0x14, "MaxAmbiguousRecipients")
        code_pages[10].add(0x15, "CertificateCount")
        code_pages[10].add(0x16, "Availability")
        code_pages[10].add(0x17, "StartTime")
        code_pages[10].add(0x18, "EndTime")
        code_pages[10].add(0x19, "MergedFreeBusy")
        code_pages[10].add(0x1A, "Picture")
        code_pages[10].add(0x1B, "MaxSize")
        code_pages[10].add(0x1C, "Data")
        code_pages[10].add(0x1D, "MaxPictures")


        # Code Page 11: ValidateCert
        code_pages.update({
                        11 : code_page( "ValidateCert" , "validatecert", 11 )
                        })
        code_pages[11].add(0x05, "ValidateCert")
        code_pages[11].add(0x06, "Certificates")
        code_pages[11].add(0x07, "Certificate")
        code_pages[11].add(0x08, "CertificateChain")
        code_pages[11].add(0x09, "CheckCRL")
        code_pages[11].add(0x0A, "Status")


        # Code Page 12: Contacts2
        code_pages.update({
                        12 : code_page( "Contacts2" , "contacts2", 12 )
                        })
        code_pages[12].add(0x05, "CustomerId")
        code_pages[12].add(0x06, "GovernmentId")
        code_pages[12].add(0x07, "IMAddress")
        code_pages[12].add(0x08, "IMAddress2")
        code_pages[12].add(0x09, "IMAddress3")
        code_pages[12].add(0x0A, "ManagerName")
        code_pages[12].add(0x0B, "CompanyMainPhone")
        code_pages[12].add(0x0C, "AccountName")
        code_pages[12].add(0x0D, "NickName")
        code_pages[12].add(0x0E, "MMS")


        # Code Page 13: Ping
        code_pages.update({
                        13 : code_page( "Ping" , "ping", 13 )
                        })
        code_pages[13].add(0x05, "Ping")
        code_pages[13].add(0x06, "AutdState")  # Per MS-ASWBXML, this tag is not used by protocol
        code_pages[13].add(0x07, "Status")
        code_pages[13].add(0x08, "HeartbeatInterval")
        code_pages[13].add(0x09, "Folders")
        code_pages[13].add(0x0A, "Folder")
        code_pages[13].add(0x0B, "Id")
        code_pages[13].add(0x0C, "Class")
        code_pages[13].add(0x0D, "MaxFolders")


        # Code Page 14: Provision
        code_pages.update({
                        14 : code_page( "Provision" , "provision", 14 )
                        })
        code_pages[14].add(0x05, "Provision")
        code_pages[14].add(0x06, "Policies")
        code_pages[14].add(0x07, "Policy")
        code_pages[14].add(0x08, "PolicyType")
        code_pages[14].add(0x09, "PolicyKey")
        code_pages[14].add(0x0A, "Data")
        code_pages[14].add(0x0B, "Status")
        code_pages[14].add(0x0C, "RemoteWipe")
        code_pages[14].add(0x0D, "EASProvisionDoc")
        code_pages[14].add(0x0E, "DevicePasswordEnabled")
        code_pages[14].add(0x0F, "AlphanumericDevicePasswordRequired")
        #code_pages[14].add(0x10, "DeviceEncryptionEnabled")
        code_pages[14].add(0x10, "RequireStorageCardEncryption")
        code_pages[14].add(0x11, "PasswordRecoveryEnabled")
        code_pages[14].add(0x13, "AttachmentsEnabled")
        code_pages[14].add(0x14, "MinDevicePasswordLength")
        code_pages[14].add(0x15, "MaxInactivityTimeDeviceLock")
        code_pages[14].add(0x16, "MaxDevicePasswordFailedAttempts")
        code_pages[14].add(0x17, "MaxAttachmentSize")
        code_pages[14].add(0x18, "AllowSimpleDevicePassword")
        code_pages[14].add(0x19, "DevicePasswordExpiration")
        code_pages[14].add(0x1A, "DevicePasswordHistory")
        code_pages[14].add(0x1B, "AllowStorageCard")
        code_pages[14].add(0x1C, "AllowCamera")
        code_pages[14].add(0x1D, "RequireDeviceEncryption")
        code_pages[14].add(0x1E, "AllowUnsignedApplications")
        code_pages[14].add(0x1F, "AllowUnsignedInstallationPackages")
        code_pages[14].add(0x20, "MinDevicePasswordComplexCharacters")
        code_pages[14].add(0x21, "AllowWiFi")
        code_pages[14].add(0x22, "AllowTextMessaging")
        code_pages[14].add(0x23, "AllowPOPIMAPEmail")
        code_pages[14].add(0x24, "AllowBluetooth")
        code_pages[14].add(0x25, "AllowIrDA")
        code_pages[14].add(0x26, "RequireManualSyncWhenRoaming")
        code_pages[14].add(0x27, "AllowDesktopSync")
        code_pages[14].add(0x28, "MaxCalendarAgeFilter")
        code_pages[14].add(0x29, "AllowHTMLEmail")
        code_pages[14].add(0x2A, "MaxEmailAgeFilter")
        code_pages[14].add(0x2B, "MaxEmailBodyTruncationSize")
        code_pages[14].add(0x2C, "MaxEmailHTMLBodyTruncationSize")
        code_pages[14].add(0x2D, "RequireSignedSMIMEMessages")
        code_pages[14].add(0x2E, "RequireEncryptedSMIMEMessages")
        code_pages[14].add(0x2F, "RequireSignedSMIMEAlgorithm")
        code_pages[14].add(0x30, "RequireEncryptionSMIMEAlgorithm")
        code_pages[14].add(0x31, "AllowSMIMEEncryptionAlgorithmNegotiation")
        code_pages[14].add(0x32, "AllowSMIMESoftCerts")
        code_pages[14].add(0x33, "AllowBrowser")
        code_pages[14].add(0x34, "AllowConsumerEmail")
        code_pages[14].add(0x35, "AllowRemoteDesktop")
        code_pages[14].add(0x36, "AllowInternetSharing")
        code_pages[14].add(0x37, "UnapprovedInROMApplicationList")
        code_pages[14].add(0x38, "ApplicationName")
        code_pages[14].add(0x39, "ApprovedApplicationList")
        code_pages[14].add(0x3A, "Hash")


        # Code Page 15: Search
        code_pages.update({
                        15 : code_page( "Search" , "search", 15 )
                        })
        code_pages[15].add(0x05, "Search")
        code_pages[15].add(0x07, "Store")
        code_pages[15].add(0x08, "Name")
        code_pages[15].add(0x09, "Query")
        code_pages[15].add(0x0A, "Options")
        code_pages[15].add(0x0B, "Range")
        code_pages[15].add(0x0C, "Status")
        code_pages[15].add(0x0D, "Response")
        code_pages[15].add(0x0E, "Result")
        code_pages[15].add(0x0F, "Properties")
        code_pages[15].add(0x10, "Total")
        code_pages[15].add(0x11, "EqualTo")
        code_pages[15].add(0x12, "Value")
        code_pages[15].add(0x13, "And")
        code_pages[15].add(0x14, "Or")
        code_pages[15].add(0x15, "FreeText")
        code_pages[15].add(0x17, "DeepTraversal")
        code_pages[15].add(0x18, "LongId")
        code_pages[15].add(0x19, "RebuildResults")
        code_pages[15].add(0x1A, "LessThan")
        code_pages[15].add(0x1B, "GreaterThan")
        code_pages[15].add(0x1E, "UserName")
        code_pages[15].add(0x1F, "Password")
        code_pages[15].add(0x20, "ConversationId")
        code_pages[15].add(0x21, "Picture")
        code_pages[15].add(0x22, "MaxSize")
        code_pages[15].add(0x23, "MaxPictures")


        # Code Page 16: GAL
        code_pages.update({
                        16 : code_page( "GAL" , "gal", 16 )
                        })
        code_pages[16].add(0x05, "DisplayName")
        code_pages[16].add(0x06, "Phone")
        code_pages[16].add(0x07, "Office")
        code_pages[16].add(0x08, "Title")
        code_pages[16].add(0x09, "Company")
        code_pages[16].add(0x0A, "Alias")
        code_pages[16].add(0x0B, "FirstName")
        code_pages[16].add(0x0C, "LastName")
        code_pages[16].add(0x0D, "HomePhone")
        code_pages[16].add(0x0E, "MobilePhone")
        code_pages[16].add(0x0F, "EmailAddress")
        code_pages[16].add(0x10, "Picture")
        code_pages[16].add(0x11, "Status")
        code_pages[16].add(0x12, "Data")


        # Code Page 17: AirSyncBase
        code_pages.update({
                        17 : code_page( "AirSyncBase" , "airsyncbase", 17 )
                        })
        code_pages[17].add(0x05, "BodyPreference")
        code_pages[17].add(0x06, "Type")
        code_pages[17].add(0x07, "TruncationSize")
        code_pages[17].add(0x08, "AllOrNone")
        code_pages[17].add(0x0A, "Body")
        code_pages[17].add(0x0B, "Data")
        code_pages[17].add(0x0C, "EstimatedDataSize")
        code_pages[17].add(0x0D, "Truncated")
        code_pages[17].add(0x0E, "Attachments")
        code_pages[17].add(0x0F, "Attachment")
        code_pages[17].add(0x10, "DisplayName")
        code_pages[17].add(0x11, "FileReference")
        code_pages[17].add(0x12, "Method")
        code_pages[17].add(0x13, "ContentId")
        code_pages[17].add(0x14, "ContentLocation")
        code_pages[17].add(0x15, "IsInline")
        code_pages[17].add(0x16, "NativeBodyType")
        code_pages[17].add(0x17, "ContentType")
        code_pages[17].add(0x18, "Preview")
        code_pages[17].add(0x19, "BodyPartPreference")
        code_pages[17].add(0x1A, "BodyPart")
        code_pages[17].add(0x1B, "Status")


        # Code Page 18: Settings
        code_pages.update({
                        18 : code_page( "Settings" , "settings", 18 )
                        })
        code_pages[18].add(0x05, "Settings")
        code_pages[18].add(0x06, "Status")
        code_pages[18].add(0x07, "Get")
        code_pages[18].add(0x08, "Set")
        code_pages[18].add(0x09, "Oof")
        code_pages[18].add(0x0A, "OofState")
        code_pages[18].add(0x0B, "StartTime")
        code_pages[18].add(0x0C, "EndTime")
        code_pages[18].add(0x0D, "OofMessage")
        code_pages[18].add(0x0E, "AppliesToInternal")
        code_pages[18].add(0x0F, "AppliesToExternalKnown")
        code_pages[18].add(0x10, "AppliesToExternalUnknown")
        code_pages[18].add(0x11, "Enabled")
        code_pages[18].add(0x12, "ReplyMessage")
        code_pages[18].add(0x13, "BodyType")
        code_pages[18].add(0x14, "DevicePassword")
        code_pages[18].add(0x15, "Password")
        code_pages[18].add(0x16, "DeviceInformation")
        code_pages[18].add(0x17, "Model")
        code_pages[18].add(0x18, "IMEI")
        code_pages[18].add(0x19, "FriendlyName")
        code_pages[18].add(0x1A, "OS")
        code_pages[18].add(0x1B, "OSLanguage")
        code_pages[18].add(0x1C, "PhoneNumber")
        code_pages[18].add(0x1D, "UserInformation")
        code_pages[18].add(0x1E, "EmailAddresses")
        code_pages[18].add(0x1F, "SMTPAddress")
        code_pages[18].add(0x20, "UserAgent")
        code_pages[18].add(0x21, "EnableOutboundSMS")
        code_pages[18].add(0x22, "MobileOperator")
        code_pages[18].add(0x23, "PrimarySmtpAddress")
        code_pages[18].add(0x24, "Accounts")
        code_pages[18].add(0x25, "Account")
        code_pages[18].add(0x26, "AccountId")
        code_pages[18].add(0x27, "AccountName")
        code_pages[18].add(0x28, "UserDisplayName")
        code_pages[18].add(0x29, "SendDisabled")
        code_pages[18].add(0x2B, "RightsManagementInformation")


        # Code Page 19: DocumentLibrary
        code_pages.update({
                        19 : code_page( "DocumentLibrary" , "documentlibrary", 19 )
                        })
        code_pages[19].add(0x05, "LinkId")
        code_pages[19].add(0x06, "DisplayName")
        code_pages[19].add(0x07, "IsFolder")
        code_pages[19].add(0x08, "CreationDate")
        code_pages[19].add(0x09, "LastModifiedDate")
        code_pages[19].add(0x0A, "IsHidden")
        code_pages[19].add(0x0B, "ContentLength")
        code_pages[19].add(0x0C, "ContentType")


        # Code Page 20: ItemOperations
        code_pages.update({
                        20 : code_page( "ItemOperations" , "itemoperations", 20 )
                        })
        code_pages[20].add(0x05, "ItemOperations")
        code_pages[20].add(0x06, "Fetch")
        code_pages[20].add(0x07, "Store")
        code_pages[20].add(0x08, "Options")
        code_pages[20].add(0x09, "Range")
        code_pages[20].add(0x0A, "Total")
        code_pages[20].add(0x0B, "Properties")
        code_pages[20].add(0x0C, "Data")
        code_pages[20].add(0x0D, "Status")
        code_pages[20].add(0x0E, "Response")
        code_pages[20].add(0x0F, "Version")
        code_pages[20].add(0x10, "Schema")
        code_pages[20].add(0x11, "Part")
        code_pages[20].add(0x12, "EmptyFolderContents")
        code_pages[20].add(0x13, "DeleteSubFolders")
        code_pages[20].add(0x14, "UserName")
        code_pages[20].add(0x15, "Password")
        code_pages[20].add(0x16, "Move")
        code_pages[20].add(0x17, "DstFldId")
        code_pages[20].add(0x18, "ConversationId")
        code_pages[20].add(0x19, "MoveAlways")


        # Code Page 21: ComposeMail
        code_pages.update({
                        21 : code_page( "ComposeMail" , "composemail", 21 )
                        })
        code_pages[21].add(0x05, "SendMail")
        code_pages[21].add(0x06, "SmartForward")
        code_pages[21].add(0x07, "SmartReply")
        code_pages[21].add(0x08, "SaveInSentItems")
        code_pages[21].add(0x09, "ReplaceMime")
        code_pages[21].add(0x0B, "Source")
        code_pages[21].add(0x0C, "FolderId")
        code_pages[21].add(0x0D, "ItemId")
        code_pages[21].add(0x0E, "LongId")
        code_pages[21].add(0x0F, "InstanceId")
        code_pages[21].add(0x10, "Mime")
        code_pages[21].add(0x11, "ClientId")
        code_pages[21].add(0x12, "Status")
        code_pages[21].add(0x13, "AccountId")


        # Code Page 22: Email2
        code_pages.update({
                        22 : code_page( "Email2" , "email2", 22 )
                        })
        code_pages[22].add(0x05, "UmCallerID")
        code_pages[22].add(0x06, "UmUserNotes")
        code_pages[22].add(0x07, "UmAttDuration")
        code_pages[22].add(0x08, "UmAttOrder")
        code_pages[22].add(0x09, "ConversationId")
        code_pages[22].add(0x0A, "ConversationIndex")
        code_pages[22].add(0x0B, "LastVerbExecuted")
        code_pages[22].add(0x0C, "LastVerbExecutionTime")
        code_pages[22].add(0x0D, "ReceivedAsBcc")
        code_pages[22].add(0x0E, "Sender")
        code_pages[22].add(0x0F, "CalendarType")
        code_pages[22].add(0x10, "IsLeapMonth")
        code_pages[22].add(0x11, "AccountId")
        code_pages[22].add(0x12, "FirstDayOfWeek")
        code_pages[22].add(0x13, "MeetingMessageType")


        # Code Page 23: Notes
        code_pages.update({
                        23 : code_page( "Notes" , "notes", 23 )
                        })
        code_pages[23].add(0x05, "Subject")
        code_pages[23].add(0x06, "MessageClass")
        code_pages[23].add(0x07, "LastModifiedDate")
        code_pages[23].add(0x08, "Categories")
        code_pages[23].add(0x09, "Category")


        # Code Page 24: RightsManagement
        code_pages.update({
                        24 : code_page( "RightsManagement" , "rightsmanagement", 24 )
                        })
        code_pages[24].add(0x05, "RightsManagementSupport")
        code_pages[24].add(0x06, "RightsManagementTemplates")
        code_pages[24].add(0x07, "RightsManagementTemplate")
        code_pages[24].add(0x08, "RightsManagementLicense")
        code_pages[24].add(0x09, "EditAllowed")
        code_pages[24].add(0x0A, "ReplyAllowed")
        code_pages[24].add(0x0B, "ReplyAllAllowed")
        code_pages[24].add(0x0C, "ForwardAllowed")
        code_pages[24].add(0x0D, "ModifyRecipientsAllowed")
        code_pages[24].add(0x0E, "ExtractAllowed")
        code_pages[24].add(0x0F, "PrintAllowed")
        code_pages[24].add(0x10, "ExportAllowed")
        code_pages[24].add(0x11, "ProgrammaticAccessAllowed")
        code_pages[24].add(0x12, "Owner")
        code_pages[24].add(0x13, "ContentExpiryDate")
        code_pages[24].add(0x14, "TemplateID")
        code_pages[24].add(0x15, "TemplateName")
        code_pages[24].add(0x16, "TemplateDescription")
        code_pages[24].add(0x17, "ContentOwner")
        code_pages[24].add(0x18, "RemoveRightsManagementDistribution")

        cp_shorthand = {"rm":"RightsManagement"}

        return code_pages, cp_shorthand
