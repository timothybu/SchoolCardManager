# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administratorsinfo(models.Model):
    aaccount = models.CharField(primary_key=True, max_length=12)
    apassword = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'administratorsinfo'


class AqInternetAgentPrivs(models.Model):
    agent_name = models.ForeignKey('AqInternetAgents', models.DO_NOTHING, db_column='agent_name')
    db_username = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'aq$_internet_agent_privs'
        unique_together = (('agent_name', 'db_username'),)


class AqInternetAgents(models.Model):
    agent_name = models.CharField(primary_key=True, max_length=512)
    protocol = models.BigIntegerField()
    spare1 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_internet_agents'


class AqKeyShardMap(models.Model):
    queue = models.FloatField()
    key = models.CharField(max_length=128)
    shard = models.FloatField()
    delay_shard = models.FloatField()

    class Meta:
        managed = False
        db_table = 'aq$_key_shard_map'
        unique_together = (('queue', 'key'),)


class AqQueueTables(models.Model):
    schema = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    udata_type = models.FloatField()
    objno = models.FloatField(primary_key=True)
    flags = models.FloatField()
    sort_cols = models.FloatField()
    timezone = models.CharField(max_length=64, blank=True, null=True)
    table_comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_queue_tables'


class AqQueues(models.Model):
    oid = models.TextField(primary_key=True)  # This field type is a guess.
    eventid = models.FloatField()
    name = models.CharField(max_length=128)
    table_objno = models.FloatField()
    usage = models.FloatField()
    enable_flag = models.FloatField()
    max_retries = models.FloatField(blank=True, null=True)
    retry_delay = models.FloatField(blank=True, null=True)
    properties = models.FloatField(blank=True, null=True)
    ret_time = models.FloatField(blank=True, null=True)
    queue_comment = models.CharField(max_length=2000, blank=True, null=True)
    subscribers = models.TextField(blank=True, null=True)  # This field type is a guess.
    memory_threshold = models.FloatField(blank=True, null=True)
    service_name = models.CharField(max_length=64, blank=True, null=True)
    network_name = models.CharField(max_length=256, blank=True, null=True)
    sub_oid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sharded = models.FloatField(blank=True, null=True)
    base_queue = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_queues'
        unique_together = (('name', 'table_objno'),)


class AqSchedules(models.Model):
    oid = models.TextField(primary_key=True)  # This field type is a guess.
    destination = models.CharField(max_length=390)
    start_time = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=8, blank=True, null=True)
    next_time = models.CharField(max_length=128, blank=True, null=True)
    latency = models.CharField(max_length=8, blank=True, null=True)
    last_time = models.DateField(blank=True, null=True)
    jobno = models.FloatField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_schedules'
        unique_together = (('oid', 'destination'),)


class Card(models.Model):
    cardno = models.CharField(primary_key=True, max_length=12)
    sno = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='sno', blank=True, null=True)
    cardmoney = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cardtime = models.DateField()
    carpassword = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card'


class Classinfo(models.Model):
    cid = models.CharField(primary_key=True, max_length=12)
    mid = models.ForeignKey('Majorinfo', models.DO_NOTHING, db_column='mid', blank=True, null=True)
    cname = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'classinfo'


class Collegeinfo(models.Model):
    cid = models.CharField(primary_key=True, max_length=12)
    cname = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'collegeinfo'


class Costinfo(models.Model):
    cnumber = models.CharField(primary_key=True, max_length=12)
    ctime = models.DateField()
    ccardno = models.ForeignKey(Card, models.DO_NOTHING, db_column='ccardno', blank=True, null=True)
    ccost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costinfo'


class Fillinfo(models.Model):
    rnumber = models.CharField(primary_key=True, max_length=12)
    rtime = models.DateField()
    rcardno = models.ForeignKey(Card, models.DO_NOTHING, db_column='rcardno', blank=True, null=True)
    rmoney = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fillinfo'


class Help(models.Model):
    topic = models.CharField(primary_key=True, max_length=50)
    seq = models.FloatField()
    info = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help'
        unique_together = (('topic', 'seq'),)


class LogmnrAgeSpill(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xidusn = models.FloatField()
    xidslt = models.FloatField()
    xidsqn = models.FloatField()
    chunk = models.FloatField()
    sequence_field = models.FloatField(db_column='sequence#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    offset = models.FloatField(blank=True, null=True)
    spill_data = models.BinaryField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    pdbid = models.FloatField()

    class Meta:
        managed = False
        db_table = 'logmnr_age_spill$'
        unique_together = (('session_field', 'pdbid', 'xidusn', 'xidslt', 'xidsqn', 'chunk', 'sequence_field'),)


class LogmnrAttrcol(models.Model):
    intcol_field = models.FloatField(db_column='intcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=4000, blank=True, null=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_attrcol$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrAttribute(models.Model):
    version_field = models.FloatField(db_column='version#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384, blank=True, null=True)
    attribute_field = models.FloatField(db_column='attribute#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    attr_toid = models.TextField(blank=True, null=True)  # This field type is a guess.
    attr_version_field = models.FloatField(db_column='attr_version#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    synobj_field = models.FloatField(db_column='synobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    properties = models.FloatField(blank=True, null=True)
    charsetid = models.FloatField(blank=True, null=True)
    charsetform = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    precision_field = models.FloatField(db_column='precision#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    scale = models.FloatField(blank=True, null=True)
    externname = models.CharField(max_length=4000, blank=True, null=True)
    xflags = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.FloatField(blank=True, null=True)
    setter = models.FloatField(blank=True, null=True)
    getter = models.FloatField(blank=True, null=True)
    toid = models.TextField()  # This field type is a guess.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_attribute$'
        unique_together = (('logmnr_uid', 'toid', 'version_field', 'attribute_field'),)


class LogmnrCcol(models.Model):
    con_field = models.FloatField(db_column='con#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pos_field = models.FloatField(db_column='pos#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_ccol$'
        unique_together = (('logmnr_uid', 'con_field', 'intcol_field'),)


class LogmnrCdef(models.Model):
    con_field = models.FloatField(db_column='con#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cols = models.FloatField(blank=True, null=True)
    type_field = models.FloatField(db_column='type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    robj_field = models.FloatField(db_column='robj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rcon_field = models.FloatField(db_column='rcon#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    enabled = models.FloatField(blank=True, null=True)
    defer = models.FloatField(blank=True, null=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_cdef$'
        unique_together = (('logmnr_uid', 'con_field'),)


class LogmnrCol(models.Model):
    col_field = models.BigIntegerField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    segcol_field = models.BigIntegerField(db_column='segcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384, blank=True, null=True)
    type_field = models.BigIntegerField(db_column='type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    length = models.BigIntegerField(blank=True, null=True)
    precision_field = models.BigIntegerField(db_column='precision#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    scale = models.BigIntegerField(blank=True, null=True)
    null_field = models.BigIntegerField(db_column='null$', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.BigIntegerField(db_column='intcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    property = models.BigIntegerField(blank=True, null=True)
    charsetid = models.BigIntegerField(blank=True, null=True)
    charsetform = models.BigIntegerField(blank=True, null=True)
    spare1 = models.BigIntegerField(blank=True, null=True)
    spare2 = models.BigIntegerField(blank=True, null=True)
    obj_field = models.BigIntegerField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    collid = models.FloatField(blank=True, null=True)
    collintcol_field = models.FloatField(db_column='collintcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acdrrescol_field = models.FloatField(db_column='acdrrescol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnr_col$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrColtype(models.Model):
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    toid = models.TextField(blank=True, null=True)  # This field type is a guess.
    version_field = models.FloatField(db_column='version#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    packed = models.FloatField(blank=True, null=True)
    intcols = models.FloatField(blank=True, null=True)
    intcol_s = models.TextField(db_column='intcol#s', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    flags = models.FloatField(blank=True, null=True)
    typidcol_field = models.FloatField(db_column='typidcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    synobj_field = models.FloatField(db_column='synobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_coltype$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrCon(models.Model):
    owner_field = models.FloatField(db_column='owner#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384)
    con_field = models.FloatField(db_column='con#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    start_scnbas = models.FloatField(blank=True, null=True)
    start_scnwrp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_con$'
        unique_together = (('logmnr_uid', 'con_field'),)


class LogmnrContainer(models.Model):
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    con_id_field = models.FloatField(db_column='con_id#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dbid = models.FloatField()
    con_uid = models.FloatField()
    create_scnwrp = models.FloatField()
    create_scnbas = models.FloatField()
    flags = models.FloatField(blank=True, null=True)
    status = models.FloatField()
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    vsn = models.FloatField(blank=True, null=True)
    fed_root_con_id_field = models.FloatField(db_column='fed_root_con_id#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnr_container$'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrDictionary(models.Model):
    db_name = models.CharField(max_length=27, blank=True, null=True)
    db_id = models.BigIntegerField(blank=True, null=True)
    db_created = models.CharField(max_length=20, blank=True, null=True)
    db_dict_created = models.CharField(max_length=20, blank=True, null=True)
    db_dict_scn = models.BigIntegerField(blank=True, null=True)
    db_thread_map = models.TextField(blank=True, null=True)  # This field type is a guess.
    db_txn_scnbas = models.BigIntegerField(blank=True, null=True)
    db_txn_scnwrp = models.BigIntegerField(blank=True, null=True)
    db_resetlogs_change_field = models.BigIntegerField(db_column='db_resetlogs_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    db_resetlogs_time = models.CharField(max_length=20, blank=True, null=True)
    db_version_time = models.CharField(max_length=20, blank=True, null=True)
    db_redo_type_id = models.CharField(max_length=8, blank=True, null=True)
    db_redo_release = models.CharField(max_length=60, blank=True, null=True)
    db_character_set = models.CharField(max_length=192, blank=True, null=True)
    db_version = models.CharField(max_length=240, blank=True, null=True)
    db_status = models.CharField(max_length=240, blank=True, null=True)
    db_global_name = models.CharField(max_length=384, blank=True, null=True)
    db_dict_maxobjects = models.BigIntegerField(blank=True, null=True)
    db_dict_objectcount = models.BigIntegerField()
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    pdb_name = models.CharField(max_length=384, blank=True, null=True)
    pdb_id = models.FloatField(blank=True, null=True)
    pdb_uid = models.FloatField(blank=True, null=True)
    pdb_dbid = models.FloatField(blank=True, null=True)
    pdb_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    pdb_create_scn = models.FloatField(blank=True, null=True)
    pdb_count = models.FloatField(blank=True, null=True)
    pdb_global_name = models.CharField(max_length=384, blank=True, null=True)
    fed_root_con_id_field = models.FloatField(db_column='fed_root_con_id#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnr_dictionary$'


class LogmnrDictstate(models.Model):
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    start_scnbas = models.FloatField(blank=True, null=True)
    start_scnwrp = models.FloatField(blank=True, null=True)
    end_scnbas = models.FloatField(blank=True, null=True)
    end_scnwrp = models.FloatField(blank=True, null=True)
    redo_thread = models.FloatField(blank=True, null=True)
    rbasqn = models.FloatField(blank=True, null=True)
    rbablk = models.FloatField(blank=True, null=True)
    rbabyte = models.FloatField(blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_dictstate$'


class LogmnrDid(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_did = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)
    spare4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_did$'


class LogmnrEnc(models.Model):
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    owner_field = models.FloatField(db_column='owner#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    encalg = models.FloatField(blank=True, null=True)
    intalg = models.FloatField(blank=True, null=True)
    colklc = models.TextField(blank=True, null=True)  # This field type is a guess.
    klclen = models.FloatField(blank=True, null=True)
    flag = models.FloatField(blank=True, null=True)
    mkeyid = models.CharField(max_length=192)
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_enc$'
        unique_together = (('logmnr_uid', 'obj_field', 'owner_field'),)


class LogmnrError(models.Model):
    session_field = models.FloatField(db_column='session#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    time_of_error = models.DateField(blank=True, null=True)
    code = models.FloatField(blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.CharField(max_length=4000, blank=True, null=True)
    spare5 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_error$'


class LogmnrFilter(models.Model):
    session_field = models.FloatField(db_column='session#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    filter_type = models.CharField(max_length=30, blank=True, null=True)
    attr1 = models.FloatField(blank=True, null=True)
    attr2 = models.FloatField(blank=True, null=True)
    attr3 = models.FloatField(blank=True, null=True)
    attr4 = models.FloatField(blank=True, null=True)
    attr5 = models.FloatField(blank=True, null=True)
    attr6 = models.FloatField(blank=True, null=True)
    filter_scn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.DateField(blank=True, null=True)
    attr7 = models.CharField(max_length=128, blank=True, null=True)
    attr8 = models.CharField(max_length=128, blank=True, null=True)
    attr9 = models.CharField(max_length=128, blank=True, null=True)
    attr10 = models.CharField(max_length=128, blank=True, null=True)
    attr11 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_filter$'


class LogmnrGlobal(models.Model):
    high_recid_foreign = models.FloatField(blank=True, null=True)
    high_recid_deleted = models.FloatField(blank=True, null=True)
    local_reset_scn = models.FloatField(blank=True, null=True)
    local_reset_timestamp = models.FloatField(blank=True, null=True)
    version_timestamp = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.CharField(max_length=2000, blank=True, null=True)
    spare5 = models.DateField(blank=True, null=True)
    session_field = models.FloatField(db_column='session#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnr_global$'


class LogmnrGtTabInclude(models.Model):
    schema_name = models.CharField(max_length=390, blank=True, null=True)
    table_name = models.CharField(max_length=390, blank=True, null=True)
    pdb_name = models.CharField(max_length=390, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_gt_tab_include$'


class LogmnrGtUserInclude(models.Model):
    user_name = models.CharField(max_length=390, blank=True, null=True)
    user_type = models.FloatField(blank=True, null=True)
    pdb_name = models.CharField(max_length=390, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_gt_user_include$'


class LogmnrGtXidInclude(models.Model):
    xidusn = models.FloatField(blank=True, null=True)
    xidslt = models.FloatField(blank=True, null=True)
    xidsqn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)
    pdbid = models.FloatField(blank=True, null=True)
    pdb_name = models.CharField(max_length=390, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_gt_xid_include$'


class LogmnrIcol(models.Model):
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bo_field = models.FloatField(db_column='bo#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pos_field = models.FloatField(db_column='pos#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    segcol_field = models.FloatField(db_column='segcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_icol$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrIdnseq(models.Model):
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    seqobj_field = models.FloatField(db_column='seqobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    startwith = models.FloatField()
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_idnseq$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrInd(models.Model):
    bo_field = models.BigIntegerField(db_column='bo#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cols = models.BigIntegerField(blank=True, null=True)
    type_field = models.BigIntegerField(db_column='type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flags = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    obj_field = models.BigIntegerField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_ind$'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrIndcompart(models.Model):
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dataobj_field = models.FloatField(db_column='dataobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bo_field = models.FloatField(db_column='bo#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_field = models.FloatField(db_column='part#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_indcompart$'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrIndpart(models.Model):
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bo_field = models.FloatField(db_column='bo#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_field = models.FloatField(db_column='part#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ts_field = models.FloatField(db_column='ts#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_indpart$'
        unique_together = (('logmnr_uid', 'obj_field', 'bo_field'),)


class LogmnrIndsubpart(models.Model):
    obj_field = models.BigIntegerField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dataobj_field = models.BigIntegerField(db_column='dataobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pobj_field = models.BigIntegerField(db_column='pobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subpart_field = models.BigIntegerField(db_column='subpart#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ts_field = models.BigIntegerField(db_column='ts#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_indsubpart$'
        unique_together = (('logmnr_uid', 'obj_field', 'pobj_field'),)


class LogmnrKopm(models.Model):
    length = models.FloatField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=384)
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_kopm$'
        unique_together = (('logmnr_uid', 'name'),)


class LogmnrLob(models.Model):
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lobj_field = models.FloatField(db_column='lobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    chunk = models.FloatField()
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_lob$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrLobfrag(models.Model):
    fragobj_field = models.FloatField(db_column='fragobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    parentobj_field = models.FloatField(db_column='parentobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tabfragobj_field = models.FloatField(db_column='tabfragobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indfragobj_field = models.FloatField(db_column='indfragobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    frag_field = models.FloatField(db_column='frag#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_lobfrag$'
        unique_together = (('logmnr_uid', 'fragobj_field'),)


class LogmnrLog(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    thread_field = models.FloatField(db_column='thread#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sequence_field = models.FloatField(db_column='sequence#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_change_field = models.FloatField(db_column='first_change#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    next_change_field = models.FloatField(db_column='next_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_time = models.DateField(blank=True, null=True)
    next_time = models.DateField(blank=True, null=True)
    file_name = models.CharField(max_length=513, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    info = models.CharField(max_length=32, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    dict_begin = models.CharField(max_length=3, blank=True, null=True)
    dict_end = models.CharField(max_length=3, blank=True, null=True)
    status_info = models.CharField(max_length=32, blank=True, null=True)
    db_id = models.FloatField()
    resetlogs_change_field = models.FloatField(db_column='resetlogs_change#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    reset_timestamp = models.FloatField()
    prev_resetlogs_change_field = models.FloatField(db_column='prev_resetlogs_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    prev_reset_timestamp = models.FloatField(blank=True, null=True)
    blocks = models.FloatField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    contents = models.FloatField(blank=True, null=True)
    recid = models.FloatField(blank=True, null=True)
    recstamp = models.FloatField(blank=True, null=True)
    mark_delete_timestamp = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_log$'
        unique_together = (('session_field', 'thread_field', 'sequence_field', 'first_change_field', 'db_id', 'resetlogs_change_field', 'reset_timestamp'),)


class LogmnrLogmnrBuildlog(models.Model):
    build_date = models.CharField(max_length=20, blank=True, null=True)
    db_txn_scnbas = models.FloatField(blank=True, null=True)
    db_txn_scnwrp = models.FloatField(blank=True, null=True)
    current_build_state = models.FloatField(blank=True, null=True)
    completion_status = models.FloatField(blank=True, null=True)
    marked_log_file_low_scn = models.FloatField(blank=True, null=True)
    initial_xid = models.CharField(max_length=22)
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    cdb_xid = models.CharField(max_length=22, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_logmnr_buildlog'
        unique_together = (('logmnr_uid', 'initial_xid'),)


class LogmnrNtab(models.Model):
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ntab_field = models.FloatField(db_column='ntab#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=4000, blank=True, null=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_ntab$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrObj(models.Model):
    objv_field = models.BigIntegerField(db_column='objv#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    owner_field = models.BigIntegerField(db_column='owner#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384, blank=True, null=True)
    namespace = models.BigIntegerField(blank=True, null=True)
    subname = models.CharField(max_length=384, blank=True, null=True)
    type_field = models.BigIntegerField(db_column='type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    oid_field = models.TextField(db_column='oid$', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    remoteowner = models.CharField(max_length=384, blank=True, null=True)
    linkname = models.CharField(max_length=384, blank=True, null=True)
    flags = models.BigIntegerField(blank=True, null=True)
    spare3 = models.BigIntegerField(blank=True, null=True)
    stime = models.DateField(blank=True, null=True)
    obj_field = models.BigIntegerField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    start_scnbas = models.FloatField(blank=True, null=True)
    start_scnwrp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_obj$'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrOpqtype(models.Model):
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    lobcol = models.FloatField(blank=True, null=True)
    objcol = models.FloatField(blank=True, null=True)
    extracol = models.FloatField(blank=True, null=True)
    schemaoid = models.TextField(blank=True, null=True)  # This field type is a guess.
    elemnum = models.FloatField(blank=True, null=True)
    schemaurl = models.CharField(max_length=4000, blank=True, null=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_opqtype$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrParameter(models.Model):
    session_field = models.FloatField(db_column='session#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384)
    value = models.CharField(max_length=2000, blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_parameter$'


class LogmnrPartobj(models.Model):
    parttype = models.FloatField(blank=True, null=True)
    partcnt = models.FloatField(blank=True, null=True)
    partkeycols = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    defts_field = models.FloatField(db_column='defts#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    defpctfree = models.FloatField(blank=True, null=True)
    defpctused = models.FloatField(blank=True, null=True)
    defpctthres = models.FloatField(blank=True, null=True)
    definitrans = models.FloatField(blank=True, null=True)
    defmaxtrans = models.FloatField(blank=True, null=True)
    deftiniexts = models.FloatField(blank=True, null=True)
    defextsize = models.FloatField(blank=True, null=True)
    defminexts = models.FloatField(blank=True, null=True)
    defmaxexts = models.FloatField(blank=True, null=True)
    defextpct = models.FloatField(blank=True, null=True)
    deflists = models.FloatField(blank=True, null=True)
    defgroups = models.FloatField(blank=True, null=True)
    deflogging = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    definclcol = models.FloatField(blank=True, null=True)
    parameters = models.CharField(max_length=3000, blank=True, null=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_partobj$'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrPdbInfo(models.Model):
    logmnr_did = models.FloatField(primary_key=True)
    logmnr_mdh = models.FloatField()
    pdb_name = models.CharField(max_length=384, blank=True, null=True)
    pdb_id = models.FloatField(blank=True, null=True)
    pdb_uid = models.FloatField(blank=True, null=True)
    plugin_scn = models.FloatField()
    unplug_scn = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)
    spare4 = models.DateTimeField(blank=True, null=True)
    pdb_global_name = models.CharField(max_length=384, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_pdb_info$'
        unique_together = (('logmnr_did', 'logmnr_mdh', 'plugin_scn'),)


class LogmnrProcessedLog(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    thread_field = models.FloatField(db_column='thread#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sequence_field = models.FloatField(db_column='sequence#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_change_field = models.FloatField(db_column='first_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    next_change_field = models.FloatField(db_column='next_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_time = models.DateField(blank=True, null=True)
    next_time = models.DateField(blank=True, null=True)
    file_name = models.CharField(max_length=513, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    info = models.CharField(max_length=32, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_processed_log$'
        unique_together = (('session_field', 'thread_field'),)


class LogmnrProfilePlsqlStats(models.Model):
    pkgowner = models.CharField(primary_key=True, max_length=384)
    pkgname = models.CharField(max_length=384)
    name = models.FloatField()
    pragmaop = models.FloatField(blank=True, null=True)
    opnum = models.FloatField(blank=True, null=True)
    tlsbyunsuppopnum = models.FloatField(blank=True, null=True)
    oggunsuppopnum = models.FloatField(blank=True, null=True)
    redosize = models.FloatField(blank=True, null=True)
    redorate = models.FloatField(blank=True, null=True)
    spare1 = models.CharField(max_length=384, blank=True, null=True)
    spare2 = models.CharField(max_length=384, blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.FloatField(blank=True, null=True)
    spare6 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_profile_plsql_stats$'
        unique_together = (('pkgowner', 'pkgname', 'name'),)


class LogmnrProfileTableStats(models.Model):
    owner = models.CharField(max_length=384, blank=True, null=True)
    name = models.CharField(max_length=384, blank=True, null=True)
    objid = models.FloatField(primary_key=True)
    opnum = models.FloatField(blank=True, null=True)
    tlsbyunsuppopnum = models.FloatField(blank=True, null=True)
    oggunsuppopnum = models.FloatField(blank=True, null=True)
    oggfetchopnum = models.FloatField(blank=True, null=True)
    oggplsqlopnum = models.FloatField(blank=True, null=True)
    partnum = models.FloatField(blank=True, null=True)
    insertnum = models.FloatField(blank=True, null=True)
    updatenum = models.FloatField(blank=True, null=True)
    deletenum = models.FloatField(blank=True, null=True)
    ddlnum = models.FloatField(blank=True, null=True)
    property1 = models.FloatField(blank=True, null=True)
    property2 = models.FloatField(blank=True, null=True)
    partitionattr = models.FloatField(blank=True, null=True)
    redosize = models.FloatField(blank=True, null=True)
    maxlobsize = models.FloatField(blank=True, null=True)
    redorate = models.FloatField(blank=True, null=True)
    spare1 = models.CharField(max_length=384, blank=True, null=True)
    spare2 = models.CharField(max_length=384, blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.FloatField(blank=True, null=True)
    spare6 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_profile_table_stats$'


class LogmnrProps(models.Model):
    value_field = models.CharField(db_column='value$', max_length=4000, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    comment_field = models.CharField(db_column='comment$', max_length=4000, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384)
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_props$'
        unique_together = (('logmnr_uid', 'name'),)


class LogmnrRefcon(models.Model):
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    reftyp = models.FloatField(blank=True, null=True)
    stabid = models.TextField(blank=True, null=True)  # This field type is a guess.
    expctoid = models.TextField(blank=True, null=True)  # This field type is a guess.
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_refcon$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrRestartCkpt(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    valid = models.FloatField(blank=True, null=True)
    ckpt_scn = models.FloatField()
    xidusn = models.FloatField()
    xidslt = models.FloatField()
    xidsqn = models.FloatField()
    session_num = models.FloatField()
    serial_num = models.FloatField()
    ckpt_info = models.BinaryField(blank=True, null=True)
    flag = models.FloatField(blank=True, null=True)
    offset = models.FloatField(blank=True, null=True)
    client_data = models.BinaryField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    pdbid = models.FloatField()

    class Meta:
        managed = False
        db_table = 'logmnr_restart_ckpt$'
        unique_together = (('session_field', 'ckpt_scn', 'xidusn', 'xidslt', 'xidsqn', 'pdbid', 'session_num', 'serial_num'),)


class LogmnrRestartCkptTxinfo(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xidusn = models.FloatField()
    xidslt = models.FloatField()
    xidsqn = models.FloatField()
    session_num = models.FloatField()
    serial_num = models.FloatField()
    flag = models.FloatField(blank=True, null=True)
    start_scn = models.FloatField(blank=True, null=True)
    effective_scn = models.FloatField()
    offset = models.FloatField(blank=True, null=True)
    tx_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_restart_ckpt_txinfo$'
        unique_together = (('session_field', 'xidusn', 'xidslt', 'xidsqn', 'session_num', 'serial_num', 'effective_scn'),)


class LogmnrSeed(models.Model):
    seed_version = models.BigIntegerField(blank=True, null=True)
    gather_version = models.BigIntegerField(blank=True, null=True)
    schemaname = models.CharField(max_length=384, blank=True, null=True)
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    objv_field = models.BigIntegerField(db_column='objv#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    table_name = models.CharField(max_length=384, blank=True, null=True)
    col_name = models.CharField(max_length=384, blank=True, null=True)
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    segcol_field = models.FloatField(db_column='segcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type_field = models.FloatField(db_column='type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    precision_field = models.FloatField(db_column='precision#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    scale = models.FloatField(blank=True, null=True)
    null_field = models.FloatField(db_column='null$')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_seed$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field'),)


class LogmnrSession(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    client_field = models.FloatField(db_column='client#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    session_name = models.CharField(unique=True, max_length=128)
    db_id = models.FloatField(blank=True, null=True)
    resetlogs_change_field = models.FloatField(db_column='resetlogs_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    session_attr = models.FloatField(blank=True, null=True)
    session_attr_verbose = models.CharField(max_length=400, blank=True, null=True)
    start_scn = models.FloatField(blank=True, null=True)
    end_scn = models.FloatField(blank=True, null=True)
    spill_scn = models.FloatField(blank=True, null=True)
    spill_time = models.DateField(blank=True, null=True)
    oldest_scn = models.FloatField(blank=True, null=True)
    resume_scn = models.FloatField(blank=True, null=True)
    global_db_name = models.CharField(max_length=384, blank=True, null=True)
    reset_timestamp = models.FloatField(blank=True, null=True)
    branch_scn = models.FloatField(blank=True, null=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    redo_compat = models.CharField(max_length=20, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    purge_scn = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.FloatField(blank=True, null=True)
    spare6 = models.DateField(blank=True, null=True)
    spare7 = models.CharField(max_length=1000, blank=True, null=True)
    spare8 = models.CharField(max_length=1000, blank=True, null=True)
    spare9 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_session$'


class LogmnrSessionActions(models.Model):
    flagsruntime = models.FloatField(blank=True, null=True)
    dropscn = models.FloatField(blank=True, null=True)
    modifytime = models.DateTimeField(blank=True, null=True)
    dispatchtime = models.DateTimeField(blank=True, null=True)
    droptime = models.DateTimeField(blank=True, null=True)
    lcrcount = models.FloatField(blank=True, null=True)
    actionname = models.CharField(max_length=30)
    logmnrsession_field = models.FloatField(db_column='logmnrsession#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    processrole_field = models.FloatField(db_column='processrole#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actiontype_field = models.FloatField(db_column='actiontype#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flagsdefinetime = models.FloatField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    xidusn = models.FloatField(blank=True, null=True)
    xidslt = models.FloatField(blank=True, null=True)
    xidsqn = models.FloatField(blank=True, null=True)
    thread_field = models.FloatField(db_column='thread#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    startscn = models.FloatField(blank=True, null=True)
    startsubscn = models.FloatField(blank=True, null=True)
    endscn = models.FloatField(blank=True, null=True)
    endsubscn = models.FloatField(blank=True, null=True)
    rbasqn = models.FloatField(blank=True, null=True)
    rbablk = models.FloatField(blank=True, null=True)
    rbabyte = models.FloatField(blank=True, null=True)
    session_field = models.FloatField(db_column='session#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    attr1 = models.FloatField(blank=True, null=True)
    attr2 = models.FloatField(blank=True, null=True)
    attr3 = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.DateTimeField(blank=True, null=True)
    spare4 = models.CharField(max_length=2000, blank=True, null=True)
    pdbid = models.FloatField(blank=True, null=True)
    pdb_name = models.CharField(max_length=390, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_session_actions$'
        unique_together = (('logmnrsession_field', 'actionname'),)


class LogmnrSessionEvolve(models.Model):
    branch_level = models.FloatField(blank=True, null=True)
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    db_id = models.FloatField()
    reset_scn = models.FloatField()
    reset_timestamp = models.FloatField()
    prev_reset_scn = models.FloatField(blank=True, null=True)
    prev_reset_timestamp = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_session_evolve$'
        unique_together = (('session_field', 'db_id', 'reset_scn', 'reset_timestamp'),)


class LogmnrShardTs(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    tablespace_name = models.CharField(max_length=90)
    chunk_number = models.FloatField()
    start_scnbas = models.FloatField(blank=True, null=True)
    start_scnwrp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_shard_ts'
        unique_together = (('logmnr_uid', 'tablespace_name'),)


class LogmnrSpill(models.Model):
    session_field = models.FloatField(db_column='session#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xidusn = models.FloatField()
    xidslt = models.FloatField()
    xidsqn = models.FloatField()
    chunk = models.FloatField()
    startidx = models.FloatField()
    endidx = models.FloatField()
    flag = models.FloatField()
    sequence_field = models.FloatField(db_column='sequence#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    spill_data = models.BinaryField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    pdbid = models.FloatField()

    class Meta:
        managed = False
        db_table = 'logmnr_spill$'
        unique_together = (('session_field', 'pdbid', 'xidusn', 'xidslt', 'xidsqn', 'chunk', 'startidx', 'endidx', 'flag', 'sequence_field'),)


class LogmnrSubcoltype(models.Model):
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    toid = models.TextField()  # This field type is a guess.
    version_field = models.FloatField(db_column='version#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcols = models.FloatField(blank=True, null=True)
    intcol_s = models.TextField(db_column='intcol#s', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    flags = models.FloatField(blank=True, null=True)
    synobj_field = models.FloatField(db_column='synobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_subcoltype$'
        unique_together = (('logmnr_uid', 'obj_field', 'intcol_field', 'toid'),)


class LogmnrTab(models.Model):
    ts_field = models.BigIntegerField(db_column='ts#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cols = models.BigIntegerField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    intcols = models.BigIntegerField(blank=True, null=True)
    kernelcols = models.BigIntegerField(blank=True, null=True)
    bobj_field = models.BigIntegerField(db_column='bobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    trigflag = models.BigIntegerField(blank=True, null=True)
    flags = models.BigIntegerField(blank=True, null=True)
    obj_field = models.BigIntegerField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    acdrflags = models.FloatField(blank=True, null=True)
    acdrtsobj_field = models.FloatField(db_column='acdrtsobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acdrrowtsintcol_field = models.FloatField(db_column='acdrrowtsintcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnr_tab$'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrTabcompart(models.Model):
    obj_field = models.BigIntegerField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bo_field = models.BigIntegerField(db_column='bo#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_field = models.BigIntegerField(db_column='part#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_tabcompart$'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrTabpart(models.Model):
    obj_field = models.BigIntegerField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ts_field = models.BigIntegerField(db_column='ts#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_field = models.FloatField(db_column='part#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bo_field = models.BigIntegerField(db_column='bo#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_tabpart$'
        unique_together = (('logmnr_uid', 'obj_field', 'bo_field'),)


class LogmnrTabsubpart(models.Model):
    obj_field = models.BigIntegerField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dataobj_field = models.BigIntegerField(db_column='dataobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pobj_field = models.BigIntegerField(db_column='pobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subpart_field = models.BigIntegerField(db_column='subpart#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ts_field = models.BigIntegerField(db_column='ts#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_tabsubpart$'
        unique_together = (('logmnr_uid', 'obj_field', 'pobj_field'),)


class LogmnrTs(models.Model):
    ts_field = models.BigIntegerField(db_column='ts#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=90, blank=True, null=True)
    owner_field = models.BigIntegerField(db_column='owner#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    blocksize = models.BigIntegerField()
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)
    start_scnbas = models.FloatField(blank=True, null=True)
    start_scnwrp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_ts$'
        unique_together = (('logmnr_uid', 'ts_field'),)


class LogmnrType(models.Model):
    version_field = models.FloatField(db_column='version#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    version = models.CharField(max_length=384, blank=True, null=True)
    tvoid = models.TextField(blank=True, null=True)  # This field type is a guess.
    typecode = models.FloatField(blank=True, null=True)
    properties = models.FloatField(blank=True, null=True)
    attributes = models.FloatField(blank=True, null=True)
    methods = models.FloatField(blank=True, null=True)
    hiddenmethods = models.FloatField(blank=True, null=True)
    supertypes = models.FloatField(blank=True, null=True)
    subtypes = models.FloatField(blank=True, null=True)
    externtype = models.FloatField(blank=True, null=True)
    externname = models.CharField(max_length=4000, blank=True, null=True)
    helperclassname = models.CharField(max_length=4000, blank=True, null=True)
    local_attrs = models.FloatField(blank=True, null=True)
    local_methods = models.FloatField(blank=True, null=True)
    typeid = models.TextField(blank=True, null=True)  # This field type is a guess.
    roottoid = models.TextField(blank=True, null=True)  # This field type is a guess.
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    supertoid = models.TextField(blank=True, null=True)  # This field type is a guess.
    hashcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    toid = models.TextField()  # This field type is a guess.
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_type$'
        unique_together = (('logmnr_uid', 'toid', 'version_field'),)


class LogmnrUid(models.Model):
    logmnr_uid = models.BigIntegerField(primary_key=True)
    logmnr_did = models.FloatField(blank=True, null=True)
    logmnr_mdh = models.FloatField(blank=True, null=True)
    pdb_name = models.CharField(max_length=384, blank=True, null=True)
    pdb_id = models.FloatField(blank=True, null=True)
    pdb_uid = models.FloatField(blank=True, null=True)
    start_scn = models.FloatField(blank=True, null=True)
    end_scn = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)
    spare4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_uid$'


class LogmnrUser(models.Model):
    user_field = models.BigIntegerField(db_column='user#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384)
    logmnr_uid = models.BigIntegerField(primary_key=True, blank=True, null=True)
    logmnr_flags = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnr_user$'
        unique_together = (('logmnr_uid', 'user_field'),)


class LogmnrcConGg(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    con_field = models.FloatField(db_column='con#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384)
    commit_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    baseobj_field = models.FloatField(db_column='baseobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    baseobjv_field = models.FloatField(db_column='baseobjv#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flags = models.FloatField()
    indexobj_field = models.FloatField(db_column='indexobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.CharField(max_length=4000, blank=True, null=True)
    spare5 = models.CharField(max_length=4000, blank=True, null=True)
    spare6 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_con_gg'
        unique_together = (('logmnr_uid', 'con_field', 'commit_scn'),)


class LogmnrcConcolGg(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    con_field = models.FloatField(db_column='con#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    commit_scn = models.FloatField()
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pos_field = models.FloatField(db_column='pos#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_concol_gg'
        unique_together = (('logmnr_uid', 'con_field', 'commit_scn', 'intcol_field'),)


class LogmnrcDbnameUidMap(models.Model):
    global_name = models.CharField(primary_key=True, max_length=384)
    logmnr_uid = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    pdb_name = models.CharField(max_length=384, blank=True, null=True)
    logmnr_mdh = models.FloatField()

    class Meta:
        managed = False
        db_table = 'logmnrc_dbname_uid_map'
        unique_together = (('global_name', 'logmnr_mdh'),)


class LogmnrcGsba(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    as_of_scn = models.FloatField()
    fdo_length = models.FloatField(blank=True, null=True)
    fdo_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    charsetid = models.FloatField(blank=True, null=True)
    ncharsetid = models.FloatField(blank=True, null=True)
    dbtimezone_len = models.FloatField(blank=True, null=True)
    dbtimezone_value = models.CharField(max_length=192, blank=True, null=True)
    logmnr_spare1 = models.FloatField(blank=True, null=True)
    logmnr_spare2 = models.FloatField(blank=True, null=True)
    logmnr_spare3 = models.CharField(max_length=1000, blank=True, null=True)
    logmnr_spare4 = models.DateField(blank=True, null=True)
    db_global_name = models.CharField(max_length=384, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_gsba'
        unique_together = (('logmnr_uid', 'as_of_scn'),)


class LogmnrcGsii(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bo_field = models.FloatField(db_column='bo#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indtype_field = models.FloatField(db_column='indtype#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    drop_scn = models.FloatField(blank=True, null=True)
    logmnr_spare1 = models.FloatField(blank=True, null=True)
    logmnr_spare2 = models.FloatField(blank=True, null=True)
    logmnr_spare3 = models.CharField(max_length=1000, blank=True, null=True)
    logmnr_spare4 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_gsii'
        unique_together = (('logmnr_uid', 'obj_field'),)


class LogmnrcGtcs(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    objv_field = models.FloatField(db_column='objv#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    segcol_field = models.FloatField(db_column='segcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    colname = models.CharField(max_length=384)
    type_field = models.FloatField(db_column='type#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    precision = models.FloatField(blank=True, null=True)
    scale = models.FloatField(blank=True, null=True)
    interval_leading_precision = models.FloatField(blank=True, null=True)
    interval_trailing_precision = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    toid = models.TextField(blank=True, null=True)  # This field type is a guess.
    charsetid = models.FloatField(blank=True, null=True)
    charsetform = models.FloatField(blank=True, null=True)
    typename = models.CharField(max_length=384, blank=True, null=True)
    fqcolname = models.CharField(max_length=4000, blank=True, null=True)
    numintcols = models.FloatField(blank=True, null=True)
    numattrs = models.FloatField(blank=True, null=True)
    adtorder = models.FloatField(blank=True, null=True)
    logmnr_spare1 = models.FloatField(blank=True, null=True)
    logmnr_spare2 = models.FloatField(blank=True, null=True)
    logmnr_spare3 = models.CharField(max_length=1000, blank=True, null=True)
    logmnr_spare4 = models.DateField(blank=True, null=True)
    logmnr_spare5 = models.FloatField(blank=True, null=True)
    logmnr_spare6 = models.FloatField(blank=True, null=True)
    logmnr_spare7 = models.FloatField(blank=True, null=True)
    logmnr_spare8 = models.FloatField(blank=True, null=True)
    logmnr_spare9 = models.FloatField(blank=True, null=True)
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xtypeschemaname = models.CharField(max_length=384, blank=True, null=True)
    xtypename = models.CharField(max_length=4000, blank=True, null=True)
    xfqcolname = models.CharField(max_length=4000, blank=True, null=True)
    xtopintcol = models.FloatField(blank=True, null=True)
    xreffedtableobjn = models.FloatField(blank=True, null=True)
    xreffedtableobjv = models.FloatField(blank=True, null=True)
    xcoltypeflags = models.FloatField(blank=True, null=True)
    xopqtypetype = models.FloatField(blank=True, null=True)
    xopqtypeflags = models.FloatField(blank=True, null=True)
    xopqlobintcol = models.FloatField(blank=True, null=True)
    xopqobjintcol = models.FloatField(blank=True, null=True)
    xxmlintcol = models.FloatField(blank=True, null=True)
    eaowner_field = models.FloatField(db_column='eaowner#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    eamkeyid = models.CharField(max_length=192, blank=True, null=True)
    eaencalg = models.FloatField(blank=True, null=True)
    eaintalg = models.FloatField(blank=True, null=True)
    eacolklc = models.TextField(blank=True, null=True)  # This field type is a guess.
    eaklclen = models.FloatField(blank=True, null=True)
    eaflags = models.FloatField(blank=True, null=True)
    logmnrderivedflags = models.FloatField(blank=True, null=True)
    collid = models.FloatField(blank=True, null=True)
    collintcol_field = models.FloatField(db_column='collintcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acdrrescol_field = models.FloatField(db_column='acdrrescol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnrc_gtcs'
        unique_together = (('logmnr_uid', 'obj_field', 'objv_field', 'intcol_field'),)


class LogmnrcGtlo(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    keyobj_field = models.FloatField(db_column='keyobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvlcnt = models.FloatField()
    baseobj_field = models.FloatField(db_column='baseobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    baseobjv_field = models.FloatField(db_column='baseobjv#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl1obj_field = models.FloatField(db_column='lvl1obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl2obj_field = models.FloatField(db_column='lvl2obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl0type_field = models.FloatField(db_column='lvl0type#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl1type_field = models.FloatField(db_column='lvl1type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl2type_field = models.FloatField(db_column='lvl2type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    owner_field = models.FloatField(db_column='owner#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ownername = models.CharField(max_length=384)
    lvl0name = models.CharField(max_length=384)
    lvl1name = models.CharField(max_length=384, blank=True, null=True)
    lvl2name = models.CharField(max_length=384, blank=True, null=True)
    intcols = models.FloatField()
    cols = models.FloatField(blank=True, null=True)
    kernelcols = models.FloatField(blank=True, null=True)
    tab_flags = models.FloatField(blank=True, null=True)
    trigflag = models.FloatField(blank=True, null=True)
    assoc_field = models.FloatField(db_column='assoc#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    obj_flags = models.FloatField(blank=True, null=True)
    ts_field = models.FloatField(db_column='ts#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tsname = models.CharField(max_length=90, blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    start_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    xidusn = models.FloatField(blank=True, null=True)
    xidslt = models.FloatField(blank=True, null=True)
    xidsqn = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    logmnr_spare1 = models.FloatField(blank=True, null=True)
    logmnr_spare2 = models.FloatField(blank=True, null=True)
    logmnr_spare3 = models.CharField(max_length=1000, blank=True, null=True)
    logmnr_spare4 = models.DateField(blank=True, null=True)
    logmnr_spare5 = models.FloatField(blank=True, null=True)
    logmnr_spare6 = models.FloatField(blank=True, null=True)
    logmnr_spare7 = models.FloatField(blank=True, null=True)
    logmnr_spare8 = models.FloatField(blank=True, null=True)
    logmnr_spare9 = models.FloatField(blank=True, null=True)
    parttype = models.FloatField(blank=True, null=True)
    subparttype = models.FloatField(blank=True, null=True)
    unsupportedcols = models.FloatField(blank=True, null=True)
    complextypecols = models.FloatField(blank=True, null=True)
    ntparentobjnum = models.FloatField(blank=True, null=True)
    ntparentobjversion = models.FloatField(blank=True, null=True)
    ntparentintcolnum = models.FloatField(blank=True, null=True)
    logmnrtloflags = models.FloatField(blank=True, null=True)
    logmnrmcv = models.CharField(max_length=30, blank=True, null=True)
    acdrflags = models.FloatField(blank=True, null=True)
    acdrtsobj_field = models.FloatField(db_column='acdrtsobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acdrrowtsintcol_field = models.FloatField(db_column='acdrrowtsintcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnrc_gtlo'
        unique_together = (('logmnr_uid', 'keyobj_field', 'baseobjv_field'),)


class LogmnrcIndGg(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=384)
    commit_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    baseobj_field = models.FloatField(db_column='baseobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    baseobjv_field = models.FloatField(db_column='baseobjv#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flags = models.FloatField()
    owner_field = models.FloatField(db_column='owner#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ownername = models.CharField(max_length=384)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.CharField(max_length=4000, blank=True, null=True)
    spare5 = models.CharField(max_length=4000, blank=True, null=True)
    spare6 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_ind_gg'
        unique_together = (('logmnr_uid', 'obj_field', 'commit_scn'),)


class LogmnrcIndcolGg(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    commit_scn = models.FloatField()
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pos_field = models.FloatField(db_column='pos#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_indcol_gg'
        unique_together = (('logmnr_uid', 'obj_field', 'commit_scn', 'intcol_field'),)


class LogmnrcSeqGg(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    commit_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    seq_flags = models.FloatField()
    owner_field = models.FloatField(db_column='owner#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ownername = models.CharField(max_length=384)
    objname = models.CharField(max_length=384)
    seqcache = models.FloatField(blank=True, null=True)
    seqinc = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)
    spare4 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_seq_gg'
        unique_together = (('logmnr_uid', 'obj_field', 'commit_scn'),)


class LogmnrcShardTs(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    tablespace_name = models.CharField(max_length=90)
    chunk_number = models.FloatField()
    start_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_shard_ts'
        unique_together = (('logmnr_uid', 'tablespace_name', 'start_scn'),)


class LogmnrcTs(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    ts_field = models.BigIntegerField(db_column='ts#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=90, blank=True, null=True)
    start_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_ts'
        unique_together = (('logmnr_uid', 'ts_field', 'start_scn'),)


class LogmnrcTspart(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ts_field = models.FloatField(db_column='ts#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    start_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrc_tspart'
        unique_together = (('logmnr_uid', 'obj_field', 'start_scn'),)


class LogmnrggcGtcs(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    obj_field = models.FloatField(db_column='obj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    objv_field = models.FloatField(db_column='objv#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    segcol_field = models.FloatField(db_column='segcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intcol_field = models.FloatField(db_column='intcol#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    colname = models.CharField(max_length=384)
    type_field = models.FloatField(db_column='type#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    length = models.FloatField(blank=True, null=True)
    precision = models.FloatField(blank=True, null=True)
    scale = models.FloatField(blank=True, null=True)
    interval_leading_precision = models.FloatField(blank=True, null=True)
    interval_trailing_precision = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    toid = models.TextField(blank=True, null=True)  # This field type is a guess.
    charsetid = models.FloatField(blank=True, null=True)
    charsetform = models.FloatField(blank=True, null=True)
    typename = models.CharField(max_length=384, blank=True, null=True)
    fqcolname = models.CharField(max_length=4000, blank=True, null=True)
    numintcols = models.FloatField(blank=True, null=True)
    numattrs = models.FloatField(blank=True, null=True)
    adtorder = models.FloatField(blank=True, null=True)
    logmnr_spare1 = models.FloatField(blank=True, null=True)
    logmnr_spare2 = models.FloatField(blank=True, null=True)
    logmnr_spare3 = models.CharField(max_length=1000, blank=True, null=True)
    logmnr_spare4 = models.DateField(blank=True, null=True)
    logmnr_spare5 = models.FloatField(blank=True, null=True)
    logmnr_spare6 = models.FloatField(blank=True, null=True)
    logmnr_spare7 = models.FloatField(blank=True, null=True)
    logmnr_spare8 = models.FloatField(blank=True, null=True)
    logmnr_spare9 = models.FloatField(blank=True, null=True)
    col_field = models.FloatField(db_column='col#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xtypeschemaname = models.CharField(max_length=384, blank=True, null=True)
    xtypename = models.CharField(max_length=4000, blank=True, null=True)
    xfqcolname = models.CharField(max_length=4000, blank=True, null=True)
    xtopintcol = models.FloatField(blank=True, null=True)
    xreffedtableobjn = models.FloatField(blank=True, null=True)
    xreffedtableobjv = models.FloatField(blank=True, null=True)
    xcoltypeflags = models.FloatField(blank=True, null=True)
    xopqtypetype = models.FloatField(blank=True, null=True)
    xopqtypeflags = models.FloatField(blank=True, null=True)
    xopqlobintcol = models.FloatField(blank=True, null=True)
    xopqobjintcol = models.FloatField(blank=True, null=True)
    xxmlintcol = models.FloatField(blank=True, null=True)
    eaowner_field = models.FloatField(db_column='eaowner#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    eamkeyid = models.CharField(max_length=192, blank=True, null=True)
    eaencalg = models.FloatField(blank=True, null=True)
    eaintalg = models.FloatField(blank=True, null=True)
    eacolklc = models.TextField(blank=True, null=True)  # This field type is a guess.
    eaklclen = models.FloatField(blank=True, null=True)
    eaflags = models.FloatField(blank=True, null=True)
    logmnrderivedflags = models.FloatField(blank=True, null=True)
    collid = models.FloatField(blank=True, null=True)
    collintcol_field = models.FloatField(db_column='collintcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acdrrescol_field = models.FloatField(db_column='acdrrescol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnrggc_gtcs'
        unique_together = (('logmnr_uid', 'obj_field', 'objv_field', 'intcol_field'),)


class LogmnrggcGtlo(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    keyobj_field = models.FloatField(db_column='keyobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvlcnt = models.FloatField()
    baseobj_field = models.FloatField(db_column='baseobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    baseobjv_field = models.FloatField(db_column='baseobjv#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl1obj_field = models.FloatField(db_column='lvl1obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl2obj_field = models.FloatField(db_column='lvl2obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl0type_field = models.FloatField(db_column='lvl0type#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl1type_field = models.FloatField(db_column='lvl1type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lvl2type_field = models.FloatField(db_column='lvl2type#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    owner_field = models.FloatField(db_column='owner#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ownername = models.CharField(max_length=384)
    lvl0name = models.CharField(max_length=384)
    lvl1name = models.CharField(max_length=384, blank=True, null=True)
    lvl2name = models.CharField(max_length=384, blank=True, null=True)
    intcols = models.FloatField()
    cols = models.FloatField(blank=True, null=True)
    kernelcols = models.FloatField(blank=True, null=True)
    tab_flags = models.FloatField(blank=True, null=True)
    trigflag = models.FloatField(blank=True, null=True)
    assoc_field = models.FloatField(db_column='assoc#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    obj_flags = models.FloatField(blank=True, null=True)
    ts_field = models.FloatField(db_column='ts#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tsname = models.CharField(max_length=90, blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    start_scn = models.FloatField()
    drop_scn = models.FloatField(blank=True, null=True)
    xidusn = models.FloatField(blank=True, null=True)
    xidslt = models.FloatField(blank=True, null=True)
    xidsqn = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    logmnr_spare1 = models.FloatField(blank=True, null=True)
    logmnr_spare2 = models.FloatField(blank=True, null=True)
    logmnr_spare3 = models.CharField(max_length=1000, blank=True, null=True)
    logmnr_spare4 = models.DateField(blank=True, null=True)
    logmnr_spare5 = models.FloatField(blank=True, null=True)
    logmnr_spare6 = models.FloatField(blank=True, null=True)
    logmnr_spare7 = models.FloatField(blank=True, null=True)
    logmnr_spare8 = models.FloatField(blank=True, null=True)
    logmnr_spare9 = models.FloatField(blank=True, null=True)
    parttype = models.FloatField(blank=True, null=True)
    subparttype = models.FloatField(blank=True, null=True)
    unsupportedcols = models.FloatField(blank=True, null=True)
    complextypecols = models.FloatField(blank=True, null=True)
    ntparentobjnum = models.FloatField(blank=True, null=True)
    ntparentobjversion = models.FloatField(blank=True, null=True)
    ntparentintcolnum = models.FloatField(blank=True, null=True)
    logmnrtloflags = models.FloatField(blank=True, null=True)
    logmnrmcv = models.CharField(max_length=30, blank=True, null=True)
    acdrflags = models.FloatField(blank=True, null=True)
    acdrtsobj_field = models.FloatField(db_column='acdrtsobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    acdrrowtsintcol_field = models.FloatField(db_column='acdrrowtsintcol#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'logmnrggc_gtlo'
        unique_together = (('logmnr_uid', 'keyobj_field', 'baseobjv_field'),)


class LogmnrpCtasPartMap(models.Model):
    logmnr_uid = models.FloatField(primary_key=True)
    baseobj_field = models.FloatField(db_column='baseobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    baseobjv_field = models.FloatField(db_column='baseobjv#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    keyobj_field = models.FloatField(db_column='keyobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_field = models.FloatField(db_column='part#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmnrp_ctas_part_map'
        unique_together = (('logmnr_uid', 'baseobjv_field', 'keyobj_field'),)


class LogmnrtMddl(models.Model):
    source_obj_field = models.FloatField(db_column='source_obj#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    source_rowid = models.TextField()  # This field type is a guess.
    dest_rowid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'logmnrt_mddl$'
        unique_together = (('source_obj_field', 'source_rowid'),)


class LogstdbyApplyMilestone(models.Model):
    session_id = models.FloatField()
    commit_scn = models.FloatField()
    commit_time = models.DateField(blank=True, null=True)
    synch_scn = models.FloatField()
    epoch = models.FloatField()
    processed_scn = models.FloatField()
    processed_time = models.DateField(blank=True, null=True)
    fetchlwm_scn = models.FloatField()
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    lwm_upd_time = models.DateField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.FloatField(blank=True, null=True)
    spare6 = models.FloatField(blank=True, null=True)
    spare7 = models.DateField(blank=True, null=True)
    pto_recovery_scn = models.FloatField(blank=True, null=True)
    pto_recovery_incarnation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$apply_milestone'


class LogstdbyApplyProgress(models.Model):
    xidusn = models.FloatField(blank=True, null=True)
    xidslt = models.FloatField(blank=True, null=True)
    xidsqn = models.FloatField(blank=True, null=True)
    commit_scn = models.FloatField(blank=True, null=True)
    commit_time = models.DateField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$apply_progress'


class LogstdbyEdsTables(models.Model):
    owner = models.CharField(primary_key=True, max_length=128)
    table_name = models.CharField(max_length=128)
    shadow_table_name = models.CharField(max_length=128, blank=True, null=True)
    base_trigger_name = models.CharField(max_length=128, blank=True, null=True)
    shadow_trigger_name = models.CharField(max_length=128, blank=True, null=True)
    dblink = models.CharField(max_length=255, blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    objv = models.FloatField(blank=True, null=True)
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sobj_field = models.FloatField(db_column='sobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ctime = models.DateTimeField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.CharField(max_length=255, blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    mview_name = models.CharField(max_length=128, blank=True, null=True)
    mview_log_name = models.CharField(max_length=128, blank=True, null=True)
    mview_trigger_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$eds_tables'
        unique_together = (('owner', 'table_name'),)


class LogstdbyEvents(models.Model):
    event_time = models.DateTimeField()
    current_scn = models.FloatField(blank=True, null=True)
    commit_scn = models.FloatField(blank=True, null=True)
    xidusn = models.FloatField(blank=True, null=True)
    xidslt = models.FloatField(blank=True, null=True)
    xidsqn = models.FloatField(blank=True, null=True)
    errval = models.FloatField(blank=True, null=True)
    event = models.CharField(max_length=2000, blank=True, null=True)
    full_event = models.TextField(blank=True, null=True)
    error = models.CharField(max_length=2000, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)
    con_name = models.CharField(max_length=30, blank=True, null=True)
    con_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$events'


class LogstdbyFlashbackScn(models.Model):
    primary_scn = models.FloatField(primary_key=True)
    primary_time = models.DateField(blank=True, null=True)
    standby_scn = models.FloatField(blank=True, null=True)
    standby_time = models.DateField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$flashback_scn'


class LogstdbyHistory(models.Model):
    stream_sequence_field = models.FloatField(db_column='stream_sequence#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lmnr_sid = models.FloatField(blank=True, null=True)
    dbid = models.FloatField(blank=True, null=True)
    first_change_field = models.FloatField(db_column='first_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    last_change_field = models.FloatField(db_column='last_change#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    source = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    first_time = models.DateField(blank=True, null=True)
    last_time = models.DateField(blank=True, null=True)
    dgname = models.CharField(max_length=255, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$history'


class LogstdbyParameters(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    value = models.CharField(max_length=2000, blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$parameters'


class LogstdbyPlsql(models.Model):
    session_id = models.FloatField(blank=True, null=True)
    start_finish = models.FloatField(blank=True, null=True)
    call_text = models.TextField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$plsql'


class LogstdbyScn(models.Model):
    obj_field = models.FloatField(db_column='obj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    objname = models.CharField(max_length=4000, blank=True, null=True)
    schema = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$scn'


class LogstdbySkip(models.Model):
    error = models.FloatField(blank=True, null=True)
    statement_opt = models.CharField(max_length=128, blank=True, null=True)
    schema = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=261, blank=True, null=True)
    use_like = models.FloatField(blank=True, null=True)
    esc = models.CharField(max_length=1, blank=True, null=True)
    proc = models.CharField(max_length=392, blank=True, null=True)
    active = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$skip'


class LogstdbySkipSupport(models.Model):
    action = models.FloatField()
    name = models.CharField(max_length=128)
    name2 = models.CharField(max_length=128, blank=True, null=True)
    name3 = models.CharField(max_length=128, blank=True, null=True)
    name4 = models.CharField(max_length=128, blank=True, null=True)
    name5 = models.CharField(max_length=128, blank=True, null=True)
    reg = models.BigIntegerField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$skip_support'


class LogstdbySkipTransaction(models.Model):
    xidusn = models.FloatField(blank=True, null=True)
    xidslt = models.FloatField(blank=True, null=True)
    xidsqn = models.FloatField(blank=True, null=True)
    active = models.FloatField(blank=True, null=True)
    commit_scn = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=2000, blank=True, null=True)
    con_name = models.CharField(max_length=384, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstdby$skip_transaction'


class Losinfo(models.Model):
    cardno = models.ForeignKey(Card, models.DO_NOTHING, db_column='cardno', primary_key=True)
    ltime = models.DateField()

    class Meta:
        managed = False
        db_table = 'losinfo'


class Majorinfo(models.Model):
    mid = models.CharField(primary_key=True, max_length=12)
    cid = models.ForeignKey(Collegeinfo, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    mname = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'majorinfo'


class MviewAdvAjg(models.Model):
    ajgid_field = models.FloatField(db_column='ajgid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ajgdeslen = models.FloatField()
    ajgdes = models.TextField()  # This field type is a guess.
    hashvalue = models.FloatField()
    frequency = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_ajg'


class MviewAdvBasetable(models.Model):
    collectionid_field = models.FloatField(db_column='collectionid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    queryid_field = models.ForeignKey('MviewAdvWorkload', models.DO_NOTHING, db_column='queryid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    owner = models.CharField(max_length=128, blank=True, null=True)
    table_name = models.CharField(max_length=128, blank=True, null=True)
    table_type = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_basetable'


class MviewAdvClique(models.Model):
    cliqueid_field = models.FloatField(db_column='cliqueid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cliquedeslen = models.FloatField()
    cliquedes = models.TextField()  # This field type is a guess.
    hashvalue = models.FloatField()
    frequency = models.FloatField()
    bytecost = models.FloatField()
    rowsize = models.FloatField()
    numrows = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mview$_adv_clique'


class MviewAdvEligible(models.Model):
    sumobjn_field = models.FloatField(db_column='sumobjn#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bytecost = models.FloatField()
    flags = models.FloatField()
    frequency = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mview$_adv_eligible'
        unique_together = (('sumobjn_field', 'runid_field'),)


class MviewAdvExceptions(models.Model):
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    owner = models.CharField(max_length=128, blank=True, null=True)
    table_name = models.CharField(max_length=128, blank=True, null=True)
    dimension_name = models.CharField(max_length=128, blank=True, null=True)
    relationship = models.CharField(max_length=11, blank=True, null=True)
    bad_rowid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mview$_adv_exceptions'


class MviewAdvFilter(models.Model):
    filterid_field = models.FloatField(db_column='filterid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subfilternum_field = models.FloatField(db_column='subfilternum#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subfiltertype = models.FloatField()
    str_value = models.CharField(max_length=1028, blank=True, null=True)
    num_value1 = models.FloatField(blank=True, null=True)
    num_value2 = models.FloatField(blank=True, null=True)
    date_value1 = models.DateField(blank=True, null=True)
    date_value2 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_filter'
        unique_together = (('filterid_field', 'subfilternum_field'),)


class MviewAdvFilterinstance(models.Model):
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    filterid_field = models.FloatField(db_column='filterid#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subfilternum_field = models.FloatField(db_column='subfilternum#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subfiltertype = models.FloatField(blank=True, null=True)
    str_value = models.CharField(max_length=1028, blank=True, null=True)
    num_value1 = models.FloatField(blank=True, null=True)
    num_value2 = models.FloatField(blank=True, null=True)
    date_value1 = models.DateField(blank=True, null=True)
    date_value2 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_filterinstance'


class MviewAdvFjg(models.Model):
    fjgid_field = models.FloatField(db_column='fjgid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ajgid_field = models.ForeignKey(MviewAdvAjg, models.DO_NOTHING, db_column='ajgid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fjgdeslen = models.FloatField()
    fjgdes = models.TextField()  # This field type is a guess.
    hashvalue = models.FloatField()
    frequency = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_fjg'


class MviewAdvGc(models.Model):
    gcid_field = models.FloatField(db_column='gcid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fjgid_field = models.ForeignKey(MviewAdvFjg, models.DO_NOTHING, db_column='fjgid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gcdeslen = models.FloatField()
    gcdes = models.TextField()  # This field type is a guess.
    hashvalue = models.FloatField()
    frequency = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_gc'


class MviewAdvInfo(models.Model):
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    seq_field = models.FloatField(db_column='seq#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type = models.FloatField()
    infolen = models.FloatField()
    info = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.FloatField(blank=True, null=True)
    flag = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_info'
        unique_together = (('runid_field', 'seq_field'),)


class MviewAdvJournal(models.Model):
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    seq_field = models.FloatField(db_column='seq#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    timestamp = models.DateField()
    flags = models.FloatField()
    num = models.FloatField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)  # This field type is a guess.
    textlen = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_journal'
        unique_together = (('runid_field', 'seq_field'),)


class MviewAdvLevel(models.Model):
    runid_field = models.ForeignKey('MviewAdvLog', models.DO_NOTHING, db_column='runid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    levelid_field = models.FloatField(db_column='levelid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dimobj_field = models.FloatField(db_column='dimobj#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flags = models.FloatField()
    tblobj_field = models.FloatField(db_column='tblobj#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    columnlist = models.TextField()  # This field type is a guess.
    levelname = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_level'
        unique_together = (('runid_field', 'levelid_field'),)


class MviewAdvLog(models.Model):
    runid_field = models.FloatField(db_column='runid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    filterid_field = models.FloatField(db_column='filterid#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    run_begin = models.DateField(blank=True, null=True)
    run_end = models.DateField(blank=True, null=True)
    run_type = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=128, blank=True, null=True)
    status = models.FloatField()
    message = models.CharField(max_length=2000, blank=True, null=True)
    completed = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    error_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_log'


class MviewAdvOutput(models.Model):
    runid_field = models.ForeignKey(MviewAdvLog, models.DO_NOTHING, db_column='runid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    output_type = models.FloatField()
    rank_field = models.FloatField(db_column='rank#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    action_type = models.CharField(max_length=6, blank=True, null=True)
    summary_owner = models.CharField(max_length=128, blank=True, null=True)
    summary_name = models.CharField(max_length=128, blank=True, null=True)
    group_by_columns = models.CharField(max_length=2000, blank=True, null=True)
    where_clause = models.CharField(max_length=2000, blank=True, null=True)
    from_clause = models.CharField(max_length=2000, blank=True, null=True)
    measures_list = models.CharField(max_length=2000, blank=True, null=True)
    fact_tables = models.CharField(max_length=1000, blank=True, null=True)
    grouping_levels = models.CharField(max_length=2000, blank=True, null=True)
    querylen = models.FloatField(blank=True, null=True)
    query_text = models.TextField(blank=True, null=True)  # This field type is a guess.
    storage_in_bytes = models.FloatField(blank=True, null=True)
    pct_performance_gain = models.FloatField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    cumulative_benefit = models.FloatField(blank=True, null=True)
    benefit_to_cost_ratio = models.FloatField()
    validated = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_output'
        unique_together = (('runid_field', 'rank_field'),)


class MviewAdvParameters(models.Model):
    parameter_name = models.CharField(primary_key=True, max_length=128)
    parameter_type = models.FloatField()
    string_value = models.CharField(max_length=30, blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    numerical_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_parameters'


class MviewAdvPlan(models.Model):
    statement_id = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=80, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)
    object_node = models.CharField(max_length=128, blank=True, null=True)
    object_owner = models.CharField(max_length=128, blank=True, null=True)
    object_name = models.CharField(max_length=128, blank=True, null=True)
    object_instance = models.BigIntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    optimizer = models.CharField(max_length=255, blank=True, null=True)
    search_columns = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    cost = models.BigIntegerField(blank=True, null=True)
    cardinality = models.BigIntegerField(blank=True, null=True)
    bytes = models.BigIntegerField(blank=True, null=True)
    other_tag = models.CharField(max_length=255, blank=True, null=True)
    partition_start = models.CharField(max_length=255, blank=True, null=True)
    partition_stop = models.CharField(max_length=255, blank=True, null=True)
    partition_id = models.BigIntegerField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)  # This field type is a guess.
    distribution = models.CharField(max_length=30, blank=True, null=True)
    cpu_cost = models.BigIntegerField(blank=True, null=True)
    io_cost = models.BigIntegerField(blank=True, null=True)
    temp_space = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_plan'


class MviewAdvPretty(models.Model):
    queryid_field = models.FloatField(db_column='queryid#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sql_text = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mview$_adv_pretty'


class MviewAdvRollup(models.Model):
    runid_field = models.ForeignKey(MviewAdvLevel, models.DO_NOTHING, db_column='runid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    clevelid_field = models.ForeignKey(MviewAdvLevel, models.DO_NOTHING, db_column='clevelid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    plevelid_field = models.ForeignKey(MviewAdvLevel, models.DO_NOTHING, db_column='plevelid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flags = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mview$_adv_rollup'
        unique_together = (('runid_field', 'clevelid_field', 'plevelid_field'),)


class MviewAdvSqldepend(models.Model):
    collectionid_field = models.FloatField(db_column='collectionid#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inst_id = models.FloatField(blank=True, null=True)
    from_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    from_hash = models.FloatField(blank=True, null=True)
    to_owner = models.CharField(max_length=128, blank=True, null=True)
    to_name = models.CharField(max_length=1000, blank=True, null=True)
    to_type = models.FloatField(blank=True, null=True)
    cardinality = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_sqldepend'


class MviewAdvTemp(models.Model):
    id_field = models.FloatField(db_column='id#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    seq_field = models.FloatField(db_column='seq#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    text = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mview$_adv_temp'


class MviewAdvWorkload(models.Model):
    queryid_field = models.FloatField(db_column='queryid#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    collectionid_field = models.FloatField(db_column='collectionid#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    collecttime = models.DateField()
    application = models.CharField(max_length=128, blank=True, null=True)
    cardinality = models.FloatField(blank=True, null=True)
    resultsize = models.FloatField(blank=True, null=True)
    uname = models.CharField(max_length=128)
    qdate = models.DateField(blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    exec_time = models.FloatField(blank=True, null=True)
    sql_text = models.TextField()  # This field type is a guess.
    sql_textlen = models.FloatField()
    sql_hash = models.FloatField(blank=True, null=True)
    sql_addr = models.TextField(blank=True, null=True)  # This field type is a guess.
    frequency = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mview$_adv_workload'


class Ol(models.Model):
    ol_name = models.CharField(max_length=128, blank=True, null=True)
    sql_text = models.TextField(blank=True, null=True)  # This field type is a guess.
    textlen = models.FloatField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)  # This field type is a guess.
    hash_value = models.FloatField(blank=True, null=True)
    hash_value2 = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    creator = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    hintcount = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ol$'


class OlHints(models.Model):
    ol_name = models.CharField(max_length=128, blank=True, null=True)
    hint_field = models.FloatField(db_column='hint#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    category = models.CharField(max_length=128, blank=True, null=True)
    hint_type = models.FloatField(blank=True, null=True)
    hint_text = models.CharField(max_length=512, blank=True, null=True)
    stage_field = models.FloatField(db_column='stage#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    node_field = models.FloatField(db_column='node#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    table_name = models.CharField(max_length=128, blank=True, null=True)
    table_tin = models.FloatField(blank=True, null=True)
    table_pos = models.FloatField(blank=True, null=True)
    ref_id = models.FloatField(blank=True, null=True)
    user_table_name = models.CharField(max_length=260, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    cardinality = models.FloatField(blank=True, null=True)
    bytes = models.FloatField(blank=True, null=True)
    hint_textoff = models.FloatField(blank=True, null=True)
    hint_textlen = models.FloatField(blank=True, null=True)
    join_pred = models.CharField(max_length=2000, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    hint_string = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ol$hints'


class OlNodes(models.Model):
    ol_name = models.CharField(max_length=128, blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    node_id = models.FloatField(blank=True, null=True)
    parent_id = models.FloatField(blank=True, null=True)
    node_type = models.FloatField(blank=True, null=True)
    node_textlen = models.FloatField(blank=True, null=True)
    node_textoff = models.FloatField(blank=True, null=True)
    node_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ol$nodes'


class RedoDb(models.Model):
    dbid = models.FloatField()
    global_dbname = models.CharField(max_length=129, blank=True, null=True)
    dbuname = models.CharField(max_length=32, blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    thread_field = models.FloatField(db_column='thread#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    resetlogs_scn_bas = models.FloatField(blank=True, null=True)
    resetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    resetlogs_time = models.FloatField()
    presetlogs_scn_bas = models.FloatField(blank=True, null=True)
    presetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    presetlogs_time = models.FloatField()
    seqno_rcv_cur = models.FloatField(blank=True, null=True)
    seqno_rcv_lo = models.FloatField(blank=True, null=True)
    seqno_rcv_hi = models.FloatField(blank=True, null=True)
    seqno_done_cur = models.FloatField(blank=True, null=True)
    seqno_done_lo = models.FloatField(blank=True, null=True)
    seqno_done_hi = models.FloatField(blank=True, null=True)
    gap_seqno = models.FloatField(blank=True, null=True)
    gap_ret = models.FloatField(blank=True, null=True)
    gap_done = models.FloatField(blank=True, null=True)
    apply_seqno = models.FloatField(blank=True, null=True)
    apply_done = models.FloatField(blank=True, null=True)
    purge_done = models.FloatField(blank=True, null=True)
    has_child = models.FloatField(blank=True, null=True)
    error1 = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    ts1 = models.FloatField(blank=True, null=True)
    ts2 = models.FloatField(blank=True, null=True)
    gap_next_scn = models.FloatField(blank=True, null=True)
    gap_next_time = models.FloatField(blank=True, null=True)
    curscn_time = models.FloatField(blank=True, null=True)
    resetlogs_scn = models.FloatField()
    presetlogs_scn = models.FloatField()
    gap_ret2 = models.FloatField(blank=True, null=True)
    curlog = models.FloatField(blank=True, null=True)
    endian = models.FloatField(blank=True, null=True)
    enqidx = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.DateField(blank=True, null=True)
    spare6 = models.CharField(max_length=65, blank=True, null=True)
    spare7 = models.CharField(max_length=129, blank=True, null=True)
    ts3 = models.FloatField(blank=True, null=True)
    curblkno = models.FloatField(blank=True, null=True)
    spare8 = models.FloatField(blank=True, null=True)
    spare9 = models.FloatField(blank=True, null=True)
    spare10 = models.FloatField(blank=True, null=True)
    spare11 = models.FloatField(blank=True, null=True)
    spare12 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redo_db'


class RedoLog(models.Model):
    dbid = models.FloatField()
    global_dbname = models.CharField(max_length=129, blank=True, null=True)
    dbuname = models.CharField(max_length=32, blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    thread_field = models.FloatField(db_column='thread#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    resetlogs_scn_bas = models.FloatField(blank=True, null=True)
    resetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    resetlogs_time = models.FloatField()
    presetlogs_scn_bas = models.FloatField(blank=True, null=True)
    presetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    presetlogs_time = models.FloatField()
    sequence_field = models.FloatField(db_column='sequence#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dupid = models.FloatField(blank=True, null=True)
    status1 = models.FloatField(blank=True, null=True)
    status2 = models.FloatField(blank=True, null=True)
    create_time = models.CharField(max_length=32, blank=True, null=True)
    close_time = models.CharField(max_length=32, blank=True, null=True)
    done_time = models.CharField(max_length=32, blank=True, null=True)
    first_scn_bas = models.FloatField(blank=True, null=True)
    first_scn_wrp = models.FloatField(blank=True, null=True)
    first_time = models.FloatField(blank=True, null=True)
    next_scn_bas = models.FloatField(blank=True, null=True)
    next_scn_wrp = models.FloatField(blank=True, null=True)
    next_time = models.FloatField(blank=True, null=True)
    first_scn = models.FloatField(blank=True, null=True)
    next_scn = models.FloatField(blank=True, null=True)
    resetlogs_scn = models.FloatField()
    blocks = models.FloatField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    old_blocks = models.FloatField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    error1 = models.FloatField(blank=True, null=True)
    error2 = models.FloatField(blank=True, null=True)
    filename = models.CharField(max_length=513, blank=True, null=True)
    ts1 = models.FloatField(blank=True, null=True)
    ts2 = models.FloatField(blank=True, null=True)
    endian = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.DateField(blank=True, null=True)
    spare6 = models.CharField(max_length=65, blank=True, null=True)
    spare7 = models.CharField(max_length=129, blank=True, null=True)
    ts3 = models.FloatField(blank=True, null=True)
    presetlogs_scn = models.FloatField()
    spare8 = models.FloatField(blank=True, null=True)
    spare9 = models.FloatField(blank=True, null=True)
    spare10 = models.FloatField(blank=True, null=True)
    old_status1 = models.FloatField(blank=True, null=True)
    old_status2 = models.FloatField(blank=True, null=True)
    old_filename = models.CharField(max_length=513, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redo_log'


class RollingConnections(models.Model):
    source_rdbid = models.FloatField(blank=True, null=True)
    dest_rdbid = models.FloatField(blank=True, null=True)
    attributes = models.FloatField(blank=True, null=True)
    service_name = models.CharField(max_length=256, blank=True, null=True)
    conn_handle = models.FloatField(blank=True, null=True)
    connect_time = models.DateTimeField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    disconnect_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    source_pid = models.FloatField(blank=True, null=True)
    dest_pid = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$connections'


class RollingDatabases(models.Model):
    rdbid = models.FloatField(blank=True, null=True)
    attributes = models.FloatField(blank=True, null=True)
    attributes2 = models.FloatField(blank=True, null=True)
    dbun = models.CharField(max_length=128, blank=True, null=True)
    dbid = models.FloatField(blank=True, null=True)
    prod_rscn = models.FloatField(blank=True, null=True)
    prod_rid = models.FloatField(blank=True, null=True)
    prod_scn = models.FloatField(blank=True, null=True)
    cons_rscn = models.FloatField(blank=True, null=True)
    cons_rid = models.FloatField(blank=True, null=True)
    cons_scn = models.FloatField(blank=True, null=True)
    engine_status = models.FloatField(blank=True, null=True)
    version = models.CharField(max_length=128, blank=True, null=True)
    redo_source = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    revision = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$databases'


class RollingDirectives(models.Model):
    directid = models.FloatField(blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    taskid = models.FloatField(blank=True, null=True)
    feature = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    target = models.FloatField(blank=True, null=True)
    flags = models.CharField(max_length=64, blank=True, null=True)
    opcode = models.FloatField(blank=True, null=True)
    p1 = models.CharField(max_length=256, blank=True, null=True)
    p2 = models.CharField(max_length=256, blank=True, null=True)
    p3 = models.CharField(max_length=256, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$directives'


class RollingEvents(models.Model):
    eventid = models.FloatField(blank=True, null=True)
    instid = models.FloatField(blank=True, null=True)
    revision = models.FloatField(blank=True, null=True)
    event_time = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    message = models.CharField(max_length=256, blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$events'


class RollingParameters(models.Model):
    scope = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    id = models.FloatField(blank=True, null=True)
    descrip = models.CharField(max_length=256, blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    datatype = models.FloatField(blank=True, null=True)
    attributes = models.FloatField(blank=True, null=True)
    curval = models.CharField(max_length=1024, blank=True, null=True)
    lstval = models.CharField(max_length=1024, blank=True, null=True)
    defval = models.CharField(max_length=1024, blank=True, null=True)
    minval = models.FloatField(blank=True, null=True)
    maxval = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$parameters'


class RollingPlan(models.Model):
    instid = models.FloatField(blank=True, null=True)
    batchid = models.FloatField(blank=True, null=True)
    directid = models.FloatField(blank=True, null=True)
    taskid = models.FloatField(blank=True, null=True)
    revision = models.FloatField(blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    progress = models.FloatField(blank=True, null=True)
    source = models.FloatField(blank=True, null=True)
    target = models.FloatField(blank=True, null=True)
    rflags = models.FloatField(blank=True, null=True)
    opcode = models.FloatField(blank=True, null=True)
    p1 = models.CharField(max_length=256, blank=True, null=True)
    p2 = models.CharField(max_length=256, blank=True, null=True)
    p3 = models.CharField(max_length=256, blank=True, null=True)
    p4 = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    exec_status = models.FloatField(blank=True, null=True)
    exec_info = models.CharField(max_length=256, blank=True, null=True)
    exec_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    post_status = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$plan'


class RollingStatistics(models.Model):
    statid = models.FloatField(blank=True, null=True)
    rdbid = models.FloatField(blank=True, null=True)
    attributes = models.FloatField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    valuestr = models.CharField(max_length=256, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valuets = models.DateTimeField(blank=True, null=True)
    valueint = models.DurationField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$statistics'


class RollingStatus(models.Model):
    revision = models.FloatField(blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    batchid = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    coordid = models.FloatField(blank=True, null=True)
    oprimary = models.FloatField(blank=True, null=True)
    fprimary = models.FloatField(blank=True, null=True)
    pid = models.FloatField(blank=True, null=True)
    instance = models.FloatField(blank=True, null=True)
    dbtotal = models.FloatField(blank=True, null=True)
    dbactive = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)
    init_time = models.DateTimeField(blank=True, null=True)
    build_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    switch_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    last_instid = models.FloatField(blank=True, null=True)
    last_batchid = models.FloatField(blank=True, null=True)
    spare1 = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling$status'


class SchedulerJobArgsTbl(models.Model):
    owner = models.CharField(max_length=128, blank=True, null=True)
    job_name = models.CharField(max_length=128, blank=True, null=True)
    argument_name = models.CharField(max_length=128, blank=True, null=True)
    argument_position = models.FloatField(blank=True, null=True)
    argument_type = models.CharField(max_length=257, blank=True, null=True)
    value = models.CharField(max_length=4000, blank=True, null=True)
    anydata_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    out_argument = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scheduler_job_args_tbl'


class SchedulerProgramArgsTbl(models.Model):
    owner = models.CharField(max_length=128)
    program_name = models.CharField(max_length=128)
    argument_name = models.CharField(max_length=128, blank=True, null=True)
    argument_position = models.FloatField()
    argument_type = models.CharField(max_length=257, blank=True, null=True)
    metadata_attribute = models.CharField(max_length=19, blank=True, null=True)
    default_value = models.CharField(max_length=4000, blank=True, null=True)
    default_anydata_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    out_argument = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scheduler_program_args_tbl'


class SqlplusProductProfile(models.Model):
    product = models.CharField(max_length=30)
    userid = models.CharField(max_length=128, blank=True, null=True)
    attribute = models.CharField(max_length=240, blank=True, null=True)
    scope = models.CharField(max_length=240, blank=True, null=True)
    numeric_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    char_value = models.CharField(max_length=240, blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    long_value = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlplus_product_profile'


class Studentinfo(models.Model):
    sno = models.CharField(primary_key=True, max_length=12)
    sname = models.CharField(max_length=8)
    ssex = models.CharField(max_length=4, blank=True, null=True)
    sage = models.DateField()
    sdept = models.ForeignKey(Collegeinfo, models.DO_NOTHING, db_column='sdept', blank=True, null=True)
    sspecial = models.ForeignKey(Majorinfo, models.DO_NOTHING, db_column='sspecial', blank=True, null=True)
    sclass = models.ForeignKey(Classinfo, models.DO_NOTHING, db_column='sclass', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentinfo'
