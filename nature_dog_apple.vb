Public Class AccessAbility

'Fields
Private aTitle As String
Private aDescription As String
Private aPriority As Integer
Private aStatus As String
Private aCategory As String

'Constructor
Public Sub New(ByVal title As String, ByVal description As String, ByVal priority As Integer, ByVal status As String, ByVal category As String)
    Me.aTitle = title
    Me.aDescription = description
    Me.aPriority = priority
    Me.aStatus = status
    Me.aCategory = category
End Sub

Public Sub SetTitle(ByVal title As String)
    Me.aTitle = title
End Sub

Public Function GetTitle() As String
    Return Me.aTitle
End Function

Public Sub SetDescription(ByVal description As String)
    Me.aDescription = description
End Sub

Public Function GetDescription() As String
    Return Me.aDescription
End Function

Public Sub SetPriority(ByVal priority As Integer)
    Me.aPriority = priority
End Sub

Public Function GetPriority() As Integer
    Return Me.aPriority
End Function

Public Sub SetStatus(ByVal status As String)
    Me.aStatus = status
End Sub

Public Function GetStatus() As String
    Return Me.aStatus
End Function

Public Sub SetCategory(ByVal category As String)
    Me.aCategory = category
End Sub

Public Function GetCategory() As String
    Return Me.aCategory
End Function

End Class