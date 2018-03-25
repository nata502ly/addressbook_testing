Feature: Group adding feature
  Descriotion

  Scenario Outline: Add new group
    Given a group list
    Given data for new group with <name>, <header>, <footer>
    When I add a new group with this data
    Then correct message is displayed
    Then a new group list is equal to the old group with this new group

    Examples:
    | name   | header      | footer      |
    | sdfdsf | new header  |  ffdbgfdbg  |
    | 124345 | $^&^*(("''  |  234234244  |
    | Новая  | Тоже самое  |  РОИЛОИЛО   |

