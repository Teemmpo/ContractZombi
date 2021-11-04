// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;
pragma experimental ABIEncoderV2;



contract ContractZoombi{
    
    address private owner;
    modifier onlyOwner(){
        require(owner==msg.sender);
        _;
    }
    constructor(address _owner){
        owner = _owner;
    }
    
    function getBalance()public view returns(uint256){
        return address(this).balance;
    }
    function getAddress()public view returns(address){
        return address(this);
    }
    
}


contract A_factoryZoombi{
    ContractZoombi[] private contractzoombi;
    address private owner;
    modifier onlyOwner(){
        require(owner==msg.sender);
        _;
    }
    constructor(){
        owner = msg.sender;
    }
    
    function create() public onlyOwner{
        
        ContractZoombi zoombi= new ContractZoombi(address(this));
        contractzoombi.push(zoombi);
    }
    
    
    function getBalanceContractZoombi(uint _index) public onlyOwner view returns(uint256){
        return contractzoombi[_index].getBalance();
    }
    function getAddressContractZoombi(uint _index) public onlyOwner view returns(address){
        return contractzoombi[_index].getAddress();
    }
    
    
}


