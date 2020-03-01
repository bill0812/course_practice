pragma solidity ^0.4.23;

// though 'emit' get syntax wrong ,but compiling is ok.
// 'emit', this word can't be lint in current vs code, don't worry
// just work in 'remix' first ,then copy code here is fine.

contract NCCUBank {
    
    //餘額 帳號=>數字
    mapping(address => uint) balances;
    
    //存款事件
    event DepositEvent(address from, uint value, uint timestamp);
    //提款事件
    event WithdrawEvent(address from, uint value, uint timestamp);
    //轉帳事件
    event TransferEvent(address from, address to, uint value, uint timestamp);
    
    //存款
    function Deposit(uint value) public {
        
        //餘額增加
        balances[msg.sender] += value;
        
        //觸發存款事件
        emit DepositEvent(msg.sender, value, now);
    }
    
    //提款
    function Withdraw(uint value) public {
        
        //require 餘額 比 要提的錢 多
        require(balances[msg.sender] >= value);
        
        //餘額減少
        balances[msg.sender] -= value;
        
        //觸發提款事件
        emit WithdrawEvent(msg.sender, value, now);
    }
    
    // 轉帳(請完成)
    function Transfer(address to, uint value) public {
        
        //require 餘額 比 要轉帳的錢 多
        require(balances[msg.sender] >= value);
        
        //將自己的餘額減少
        balances[msg.sender] -= value;
        
        //將對方的餘額增加
        balances[to] += value;
        
        //觸發轉帳事件
        emit TransferEvent(msg.sender, to, value, now);
    }
    
    //利息試算(請完成)
    function interestTrial(uint value, uint year) pure public returns(uint){
        
        //for迴圈 每一年增加6%利息
        for(uint i = 0; i < year; i++){
            value = value * 106 / 100;
        }
        //回傳value
        return value;
    }
    
    //查看自己餘額
    function getBalance() view public returns(uint){
        //回傳餘額
        return balances[msg.sender];
    }
}