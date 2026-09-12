## Section 1.5 — SRP Wrap-up

I ended up with four main classes: `BankAccount`, `AccountRepository`,
`NotificationService`, and `StatementGenerator`. Each class now has
a single responsibility, which makes the code easier to understand
and test independently. A change to the database, notification
system, or statement format can now be made without changing the
account operation logic. This reduces the risk of accidentally
breaking unrelated functionality such as deposits or withdrawals.

## Section 2.5 — OCP Wrap-up

The original design required modifying an existing if/else chain whenever a new account type was added. I changed the design by introducing the `InterestPolicy` abstraction and separate policy classes for each account type. I added `SalaryInterestPolicy` without modifying the existing Savings or Current policy classes, demonstrating that the system is open for extension but closed for modification. The main files added were `InterestPolicy.py`, `SavingsInterestPolicy.py`, `CurrentInterestPolicy.py`, `SalaryAccount.py`, and `SalaryInterestPolicy.py`.

## Section 3.2 — Why LSP Breaks

The LSP is broken because a `Square` cannot always be substituted for a `Rectangle` without changing the expected behavior. A Rectangle allows its width and height to be changed independently, while a Square must keep both dimensions equal. Therefore, code that expects normal Rectangle behavior can produce unexpected results when given a Square.

## Section 4.5 — ISP + DIP Wrap-up

I split the original fat `BankService` interface into smaller capability-based interfaces such as `Depositable`, `Withdrawable`, `Transferable`, and `StatementProvider`. This allows classes like ATM to implement only the operations they actually need. For DIP, I changed `Bank` so that it receives an `AccountRepository` through its constructor instead of creating a concrete repository internally. I also added `FileAccountRepository`, which can be swapped in from `Main.py` without changing `Bank.py`. Compared with the original design, responsibilities are now separated and high-level classes depend on abstractions rather than concrete implementations.