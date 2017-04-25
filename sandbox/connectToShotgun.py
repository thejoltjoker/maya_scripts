from Deadline.DeadlineConnect import DeadlineCon as Connect
con = Connect('PulseName', 8080)
con.Groups.GetGroupNames()
con.AuthenticationModeEnabled()
con.EnabledAuthentication(True)
con.AuthenticationModeEnabled()
con.SetAuthenticationCredentials("username", "password")
con.Groups.GetGroupNames()