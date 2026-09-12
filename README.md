## Section 1.5 — SRP Wrap-up

I ended up with four main classes: `BankAccount`, `AccountRepository`,
`NotificationService`, and `StatementGenerator`. Each class now has
a single responsibility, which makes the code easier to understand
and test independently. A change to the database, notification
system, or statement format can now be made without changing the
account operation logic. This reduces the risk of accidentally
breaking unrelated functionality such as deposits or withdrawals.