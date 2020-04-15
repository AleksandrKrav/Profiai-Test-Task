create
    definer = root@localhost procedure creator(IN json_str varchar(512))
BEGIN
    set @name = JSON_UNQUOTE(JSON_EXTRACT(json_str, '$.name'));
    set @surname = JSON_UNQUOTE(JSON_EXTRACT(json_str, '$.surname'));
    set @age = JSON_EXTRACT(json_str, '$._age');
    set @salary = JSON_EXTRACT(json_str, '$._salary');

    IF JSON_TYPE(@age) = 'NULL' THEN
        set @age = NULL;
    END IF;

     IF JSON_TYPE(@salary) = 'NULL' THEN
        set @salary = NULL;
    END IF;

    insert into app.person (name, surname, age, salary) value (@name, @surname, @age, @salary);
END;

