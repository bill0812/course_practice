pragma solidity ^0.4.23;

contract Example{

    address public teacher;

    struct grade{
        uint chinese;
        uint math;
    }

    mapping(string => grade) grades;

    event setGradesEvent(string student, uint chinese, uint math);

    modifier onlyTeacher(){
        require(msg.sender == teacher);
        _;
    }

    constructor() public {
        teacher = msg.sender;
    }

    //輸入成績
    function setGrades(string student,uint _chinese, uint _math) public onlyTeacher{
        grades[student] = grade(_chinese, _math);
        emit setGradesEvent(student, _chinese, _math);
    }

    //取得成績
    function getGrades(string student) view public returns(uint chinese, uint math){
        return (grades[student].chinese, grades[student].math);
    }

}
