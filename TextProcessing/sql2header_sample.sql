-- 
-- Import to SQLite3: sqlite3 your_db.db < tables_sqlite3.sql
--
-- Generate C++ header:
-- python D:/Code/Github/sqlpp11/scripts/ddl2cpp D:/Code/smartaccesscontrol/dbmanager/doc/tables_sqlite3.sql D:/Code/smartaccesscontrol/dbmanager/src/tables_sqlite3 dusun
-- 


PRAGMA encoding = "UTF-8";
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Houses;
DROP TABLE IF EXISTS ExtHouses;
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS FlowingPersons;
DROP TABLE IF EXISTS Devices;
DROP TABLE IF EXISTS Cards;
DROP TABLE IF EXISTS SAMCards;
DROP TABLE IF EXISTS CardPermissions;
DROP TABLE IF EXISTS CardOwnings;
DROP TABLE IF EXISTS UserHouses;
DROP TABLE IF EXISTS Accesses;
DROP TABLE IF EXISTS DeviceAlarms;
DROP TABLE IF EXISTS DeviceStatuses;


-- 区域房屋信息
CREATE TABLE Houses
(
    uuid            CHAR(36)            PRIMARY KEY NOT NULL           , -- UUID has 32 characters; allocate 36 characters for the terminating character '\0'
    cusr            CHAR(52)            NOT NULL                       , -- creation user
    _state          TINYINT                                            , -- ? 什么状态，取什么值
    cdate           DATETIME                                           , -- creation date
    udate           DATETIME                                           , -- update date
    _order          INT(11)                                            , -- ? for sorting
    code            VARCHAR(64)         NOT NULL                       , -- 区域层级编码
    cname           VARCHAR(64)         NOT NULL                       , -- Chinese name
    ename           VARCHAR(32)                                        , -- English name
    areacode        CHAR(64)            NOT NULL                       , -- 完整区域行政编码
    _type           CHAR(12)            NOT NULL                       , -- 类型: 省 1, 地级市 2, 县级市, 县 3, 乡,镇,街道 4, 社区, 村 5, 街,路,巷,里 6, 门牌号 7, 小区（农居点） 8, 楼幢 9, 单元 10, 房屋 11
    remark          CHAR(500)                                          , -- 备注
    keycode         CHAR(32)                                           , -- 区域权限因子(二级) （定长为 4位数字）
    keycode1        CHAR(12)                                           , -- 区域权限因子(一级) （定长为 4位数字）
    ifparent        TINYINT(1)                                         , -- ?
    flag            CHAR(4)             NOT NULL                       ,
    sync            TINYINT                                              -- 0 未同步; 1 已同步到公共平台
);


-- 区域房屋信息扩展
CREATE TABLE ExtHouses
(
    reluuid         CHAR(36)            NOT NULL                       ,
    jzlx            CHAR(52)                                           , -- 居住类型（数据字典）
    fwlx            CHAR(52)                                           , -- 房屋类型（数据字典）
    fwsyqlx         CHAR(52)                                           , -- 房屋所有权类型（数据字典）
    fwxxdz          CHAR(256)                                          , -- 房屋详细地址
    fczh            CHAR(52)                                           , -- 房产证号
    sspcs           CHAR(128)                                          , -- 所属派出所
    mjxx            CHAR(52)                                           , -- 民警姓名
    czyt            CHAR(256)                                          , -- 出租用途
    djba            CHAR(128)                                          , -- 登记备案
    babdate         DATETIME                                           , -- 备案开始时间
    baedate         DATETIME                                           , -- 备案结束时间
    xz              CHAR(52)                                           , -- 性质（数据字典）
    gldj            CHAR(4)                                            , -- 管理等级（数据字典）
    zlzt            CHAR(52)                                           , -- 租赁类型（数据字典）
    jshx            CHAR(52)                                           , -- 居所户型（数据字典）
    flag            CHAR(4)             NOT NULL                       ,
    sync            TINYINT                                            , -- 0 未同步; 1 已同步到公共平台
    FOREIGN KEY (reluuid) REFERENCES Houses(uuid) ON DELETE CASCADE
);


-- persons 人员信息，含：租客、房东、家属、巡防
CREATE TABLE Persons
(
    uuid            CHAR(36)            PRIMARY KEY NOT NULL           ,
    cusr            CHAR(52)            NOT NULL                       , -- creation user
    _state          TINYINT(1)                                         , -- ? 什么状态，取什么值
    cdate           DATETIME                                           , -- creation date
    udate           DATETIME                                           , -- update date
    name            CHAR(52)                                           , -- 姓名(需要加密)
    sex             TINYINT                                            , -- 性别（数据字典）
    nation          CHAR(52)                                           , -- 民族（数据字典）
    birthday        DATE                                               , -- 出生日期 yyyymmdd
    regaddress      VARCHAR(100)                                       , -- 户籍地址
    oregaddress     VARCHAR(100)                                       , -- 原户籍地址
    curaddress      VARCHAR(100)                                       , -- 现居地址
    tel             VARCHAR(20)                                        , -- 联系电话(需要加密)
    tel2            VARCHAR(20)                                        , -- 备用电话(需要加密)
    idcard          CHAR(20)            NOT NULL                       , -- 身份证号(需要加密)
    authorgan       VARCHAR(100)                                       , -- 签发机关
    avbdate         DATE                                               , -- 身份证有效期开始时间
    avedate         DATE                                               , -- 身份证有效期结束时间
    photopath       VARCHAR(4000)                                      , -- 身份证照片路径(需要加密)
    houseid         CHAR(52)                                           , -- ? 房屋居住id
    focal           TINYINT(1)                                         , -- 是否重点人员 0|否, 1|是
    proof           CHAR(52)                                           , -- 证件类型 [数据字典]
    islocal         TINYINT(1)                                         , -- 是否是本地人口
    cardisproving   TINYINT(1)                                         , -- 身份证是否被验证
    ename           VARCHAR(20)                                        , -- 姓名简拼
    flow            TINYINT(1)                                         , -- 是否是租客
    family          TINYINT(1)                                         , -- 是否是家属
    owner           TINYINT(1)                                         , -- 是否是房东
    patrol          TINYINT(1)                                         , -- 巡访
    finger1         CHAR(4000)                                         , -- 指纹采集一 (需要加密)
    finger2         CHAR(4000)                                         , -- 指纹采集二 (需要加密)
    fingertype1     CHAR(20)                                           , -- 指纹采集一类型
    fingertype2     CHAR(20)                                           , -- 指纹采集二类型
    flag            CHAR(4)            NOT NULL                        ,
    sync            TINYINT                                              -- 0 未同步; 1 已同步到公共平台    
);


-- 租客相关
CREATE TABLE FlowingPersons
(
    reluuid         CHAR(36)           NOT NULL                        ,
    polity          CHAR(52)                                           , -- 政治面貌 （数据字典）
    education       CHAR(52)                                           , -- 文化程度 （数据字典）
    comdate         DATE                                               , -- 来本地日期
    pestilence      VARCHAR(200)                                       , -- 防疫情况
    study           VARCHAR(200)                                       , -- 就学情况
    inoculability   TINYINT(1)                                         , -- 是否接种
    staycard        CHAR(20)                                           , -- 暂住证编号
    workaddress     VARCHAR(64)                                        , -- 工作地址
    marry           VARCHAR(52)                                        , -- 婚育情况
    matename        VARCHAR(20)                                        , -- 配偶姓名(需要加密)
    mateno          CHAR(20)                                           , -- 配偶身份证(需要加密)
    girls           SMALLINT                                           , -- 生育女孩子数
    boys            SMALLINT                                           , -- 生育女孩子数
    pregnantno      CHAR(20)                                           , -- 所持孕育证号码
    pregnantdate    DATETIME                                           , -- 孕检时间
    pregnantcont    VARCHAR(20)                                        , -- 落实避孕措施
    ispregnant      TINYINT(1)                                         , -- 是否怀孕
    isshbx          TINYINT(1)                                         , -- 是否参加社会保险
    isldht          TINYINT(1)                                         , -- 是否签到劳动合同
    cbdwmc          VARCHAR(64)                                        , -- 参保单位名称
    cbdwlxr         VARCHAR(20)                                        , -- 参保单位联系人(需要加密)
    cbdwlxdh        VARCHAR(20)                                        , -- 参保单位联系电话
    jyqk            VARCHAR(200)                                       , -- 教育情况
    jdxx            VARCHAR(40)                                        , -- 就读学校
    jzlx            VARCHAR(52)                                        , -- 居住类型 （数据字典）
    hjlx            VARCHAR(52)                                        , -- 户籍类型 （数据字典）
    jzzj            VARCHAR(40)                                        , -- 居住证件
    zlzt            CHAR(4)                                            , -- 租赁状态 （数据字典）
    livereason      VARCHAR(52)                                        , -- 暂住事由
    hzlsh           VARCHAR(52)                                        , -- 户主流水号
    remark          VARCHAR(200)                                       , 
    flag            CHAR(4)           NOT NULL                         ,
    sync            TINYINT                                            , -- 0 未同步; 1 已同步到公共平台
    FOREIGN KEY (reluuid) REFERENCES Persons(uuid) ON DELETE CASCADE
);


-- devices
CREATE TABLE Devices
(
    uuid            CHAR(36)          NOT NULL                         ,
    name            CHAR(64)                                           , -- 设备名称
    mac             CHAR(20)          NOT NULL                         , -- mac地址
    _type           TINYINT           NOT NULL                         , -- 设备类型 1：控制器，2：门锁
    gw_uuid         CHAR(36)                                           , -- 所属控制器（网关）的uuid
    status          TINYINT          NOT NULL                          , -- 设备状态 1：正常，2：异常，3：其他
    area_uuid       CHAR(36)          NOT NULL                         , -- 所在区域的uuid
    area_layercode  CHAR(52)          NOT NULL                         , -- 所在区域的层级编码，对应区域房屋信息中的code
    cdate           DATETIME                                           , -- 创建时间
    udate           DATETIME          NOT NULL                         , -- 更新时间
    inner_key       CHAR(32)                                           , -- 门锁对应控制器内部key
    cuser           CHAR(36)                                           , --? uuid? 创建人
    locktype        TINYINT                                            , -- 门锁类型
    flag            CHAR(4)           NOT NULL
);


-- cards 出入卡信息
CREATE TABLE Cards
(
    uuid            CHAR(36)          PRIMARY KEY NOT NULL             , -- 主键（关联表中外键引用）
    crkno           CHAR(32)          NOT NULL                         , -- 卡号
    idcode          CHAR(20)          NOT NULL                         , -- 身份信息编码( 参见杭州市规范 ) (需要加密)
    addrcode        CHAR(32)                                           , -- 住址信息编码( 参见杭州市规范 )
    udate           DATETIME          NOT NULL                         , -- update date
    cuser           CHAR(36)          NOT NULL                         , -- 创建者 uuid
    _state          TINYINT           NOT NULL                         , -- 出入卡状态(0:初始化;1:操作中;2:正常;3:挂失;4:注销)
    stime           DATETIME          NOT NULL                         , -- 有效期开始时间
    etime           DATETIME          NOT NULL                         , -- 有效期结束时间
    cdate           DATETIME          NOT NULL                         , -- 创建时间
    _key            CHAR(8)                                            , -- 区域权限因子(二级) （定长为 4位）
    mac             CHAR(30)                                           , -- ? WTF
    layercode       CHAR(52)          NOT NULL                         , -- 归属区域层级编码
    crkno4          CHAR(32)                                           , -- 卡号后4位
    key1            CHAR(8)                                            , -- 区域权限因子(一级) （定长为 4位）
    flag            CHAR(4)           NOT NULL
);


-- SAM卡信息
CREATE TABLE SAMCards
(
    _type           TINYINT           NOT NULL                         , -- sam卡类型 1：发卡SAM卡 2：门禁SAM卡
    stime           DATE              NOT NULL                         , -- 开始时间
    etime           DATE              NOT NULL                         , -- 结束时间
    area_uuid       CHAR(36)                                           , -- 区域外键
    device_uuid     CHAR(36)                                           , -- 设备外键
    status          TINYINT           NOT NULL                         , -- sam卡状态(0:正常;1:黑名单)
    cuser           CHAR(36)          NOT NULL                         , -- ? uuid? 创建者
    cdate           DATE              NOT NULL                         , -- 创建时间
    udate           DATE              NOT NULL                         , -- 更新时间
    serial_id       CHAR(32)          NOT NULL                         , -- 卡序列号
    flag            CHAR(4)           NOT NULL                         ,
    -- FOREIGN KEY (area_uuid) REFERENCES Devices(area_uuid)           ,
    FOREIGN KEY (device_uuid) REFERENCES Devices(uuid)
);


-- 出入卡权限信息
CREATE TABLE CardPermissions
(
    crk_uuid        CHAR(36)          NOT NULL                         , -- 出入卡外键
    dev_uuid        CHAR(36)          NOT NULL                         , -- 设备外键
    _state          TINYINT           NOT NULL                         , -- 状态 1：有效， 2：无效
    stime           DATE              NOT NULL                         , -- 权限开始时间
    etime           DATE                                               , -- 权限截止时间
    cuser           CHAR(36)          NOT NULL                         , -- ? uuid? in which talbe?
    cdate           DATE              NOT NULL                         , -- 创建时间
    udate           DATE              NOT NULL                         , -- 更新时间
    area_uuid       CHAR(36)                                           , -- 设备区域外键
    flag            CHAR(4)           NOT NULL                         ,
    FOREIGN KEY (crk_uuid) REFERENCES Cards(uuid)                      ,
    FOREIGN KEY (dev_uuid) REFERENCES Devices(uuid)
    -- FOREIGN KEY (area_uuid) REFERENCES Devices(area_uuid)
);


-- 人员持卡信息
CREATE TABLE CardOwnings
(
    person_uuid     CHAR(36)          NOT NULL                         , -- 人员外键
    crk_uuid        CHAR(36)          NOT NULL                         , -- 出入卡外键
    cuser           CHAR(36)          NOT NULL                         , -- ? uuid? 创建者
    cdate           DATE              NOT NULL                         , -- 创建时间
    udate           DATE              NOT NULL                         , -- 更新时间
    idcard          CHAR(36)                                           , -- ? uuid? 证件号码(需要加密)
    flag            CHAR(4)           NOT NULL                         ,
    FOREIGN KEY (person_uuid) REFERENCES Persons(uuid)                 ,
    FOREIGN KEY (crk_uuid) REFERENCES Cards(uuid)
);


-- user house  人员区域信息
CREATE TABLE UserHouses
(
    userid          CHAR(36)          NOT NULL                         , -- ? 外键引用吗
    houseid         CHAR(36)          NOT NULL                         , -- ? 外键引用吗
    _date           DATE                                               , -- 关联起始日期
    udate           DATETIME                                           , -- 记录创建日期
    reltype         TINYINT(1)        NOT NULL                         , -- 关联类型 1：租客, 2：房东, 3：家属, 4：巡访,  5：其他
    parm1           VARCHAR(52)                                        , -- 持卡类型：1：主卡， 2：附属卡
    parm2           VARCHAR(52)                                        , 
    edate           DATE                                               , -- 关联结束日期
    idcard          CHAR(52)          NOT NULL                         , -- 证件号码(需要加密)
    arcode          CHAR(64)          NOT NULL                         , -- 房屋区域层级编码
    crk_uuid        CHAR(36)                                           , -- crk外键
    crk_crkno       CHAR(52)                                           , -- 出入卡卡号
    flag            CHAR(4)           NOT NULL                         , 
    FOREIGN KEY (crk_uuid) REFERENCES Cards(uuid)
);


-- 出入记录
CREATE TABLE Accesses
(
    cardno          CHAR(36)          NOT NULL                         , -- ? uuid ? 卡号
    person_uuid     CHAR(36)          NOT NULL                         , -- 持卡人uuid
    mac             CHAR(32)          NOT NULL                         , -- 门锁 mac
    opentype        TINYINT           NOT NULL                         , -- C｜刷卡开门，F｜指纹开门，P｜密码开门，A｜其他开门
    area_uuid       CHAR(36)                                           , -- 门锁所安装区域 uuid
    slide_date      DATETIME          NOT NULL                         , -- 刷卡时间
    cdate           DATETIME          NOT NULL                         , -- 生成记录的时间
    dev_uuid        CHAR(36)                                           , -- 设备uuid
    area_code       CHAR(64)          NOT NULL                         , -- 区域 层级编码
    flag            CHAR(4)           NOT NULL                         
);


-- 设备告警信息
CREATE TABLE DeviceAlarms
(
    uuid            CHAR(36)          PRIMARY KEY NOT NULL             , -- 主键（关联表中外键引用）
    occur_date      DATETIME          NOT NULL                         , -- 告警产生时间
    cdate           DATETIME          NOT NULL                         , -- 插入本条记录的时间
    _type           TINYINT           NOT NULL                         , -- 告警类型: 强拆 1, 机械钥匙开门 11, 强行闯入 2, 非法刷卡 14
    status          TINYINT           NOT NULL                         , -- 告警状态（已处理、未处理）
    udate           DATETIME          NOT NULL                         , -- 告警处理时间
    mac             CHAR(20)                                           , -- 告警设备的mac
    area_uuid       CHAR(36)                                           , -- 告警设备所在区域的uuid
    account_uuid    CHAR(36)          NOT NULL                         , -- 告警处理人的uuid
    device_uuid     CHAR(36)                                           , -- 告警设备 uuid
    remark          CHAR(256)                                          , -- 处理意见、备注
    cardno          CHAR(36)                                           , -- ? uuid? 告警非法刷卡卡号
    flag            CHAR(4)           NOT NULL
);


-- 设备状态信息
CREATE TABLE DeviceStatuses
(
    dev_uuid        CHAR(36)          NOT NULL                         , -- 设备外键
    status          TINYINT                                            , -- 状态 0:脱机 1:联机
    hwversion       CHAR(32)                                           , -- 硬件版本号
    sfversion       CHAR(32)                                           , -- 软件版本号 
    imsi            CHAR(32)                                           , -- 控制器 imsi
    msisdn          CHAR(32)                                           , -- 控制器 msisdn
    battery         FLOAT                                              , -- 电池百分比
    temperature     FLOAT                                              , -- 温度
    signal          FLOAT                                              , -- 信号
    udate           DATETIME                                           , -- 更新时间
    cardpopedomcapacity INT                                            , -- ? 单位? 卡容量
    cardpopedomcount INT                                               , -- 门锁白名单数量
    fingercapacity  INT                                                , -- 指纹容量
    fingercount     INT                                                , -- 指纹数
    opened          TINYINT                                            , -- 门开关状态 0: 门闭合 1: 门打开
    cdate           DATETIME                                           , -- 创建时间
    cuser           CHAR(36)                                           , -- ? uuid? 创建者
    workmode        TINYINT                                            , -- ? 取值 工作状态
    powermode       TINYINT                                            , -- ? 取值 电池状态
    flag            CHAR(4)           NOT NULL
);

